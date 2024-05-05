

from buspack.https.HTTPS import HTTPS
from buspack.service.authenticator.AuthenticatorService import AuthenticatorService
from buspack.service.destination.DestinationService import DestinationService
from buspack.service.maps.mapDictObject.MapDictObject import MapDictObject
from buspack.service.maps.mapperInserter.MapperInserter import MapperInserter
from buspack.service.maps.mapperSait.MapperDestino import MapperDestino
from buspack.resources.db.DB import DB
from buspack.resources.repository.DBRepository import DBRepository
from buspack.service.maps.mapperDB.MapperDB import MapperDB
from buspack.service.maps.mapperUpdater.MapperUpdater import MapperUpdater
from sait.saitAuthenticator.SaitAuthenticator import SaitAuthenticator
from sait.saitDestinations.SaitDestinations import SaitDestinations

class InserterP1:
    
    @staticmethod
    def run():

        ## PROCESO 1:

        ## Completo Datos de los Pedidos
        saitAuthenticator = SaitAuthenticator()

        ## Realizo la Autenticacion
        httpsForAuthentication = HTTPS()
        responseAuthentication = httpsForAuthentication.responsePost({"url" : saitAuthenticator.url, "parameters" : saitAuthenticator.parametersFormData()})
        authenticatorService = AuthenticatorService(responseAuthentication)
        ## Realizo Validacion
        authenticatorService.runCheckAuthentication()

        ## Realizo la Autenticacion
        saitDestinations = SaitDestinations(responseAuthentication)

        ## Realizo el Pedido de Destinos Habilitados
        httpsForDestinations = HTTPS()
        responseDestinations = httpsForDestinations.responseGet({"url" : saitDestinations.url, "parameters" : saitDestinations.parametersFormData(), "token" : saitDestinations.headerToken()})
        destinationService = DestinationService(responseDestinations)
        destinationService.runCheckAvailableDestinations()

        ## Persisto en data los destinos
        data = responseDestinations.json().get('registros')

        # Convierto el JSON en una lista de objetos de la clase Destino
        destinos = MapperDestino.mapDestinations(data)


        ## PROCESO 2:


        # Data Wrangling

        # 1- Unicamente destinos del tipo Localidad, los que no son localidad, se les da ese tipo. Asi funciona Buspack.

        destinosFase1Localidad = list( filter( lambda x: x.isTipoLocalidad(), destinos ) )

        destinosFase1NoLocalidad = list( filter( lambda x: not( x.isTipoLocalidad() ) , destinos ) )

        # 2- Actualizo tipo a Localidad

        destinosFase1LocalidadUpdated = list( map ( lambda x: x.changeDescTipoToLocalidad(), destinosFase1NoLocalidad ) )

        destinosFase1AllLocalidad = destinosFase1Localidad + destinosFase1LocalidadUpdated


        ## PROCESO 3:
        ## Hay que pedir los datos de nuestra BD->


        # Conectar a la Base de Datos

        db = DB()
        conexion = db.connect()

        # Mapeo objetos y accedo a la BD
        mapperDB = MapperDB()
        enabledPlaces = mapperDB.mapEnabledPlace(DBRepository().getEnabledPlaces(conexion))

        ## Creo un Diccionario con Claves de IDOC para hacer la comparacion Liviana e Eficiente.

        dictSait = MapDictObject().mapDictObjectSaitByIdoc(destinosFase1AllLocalidad)
        dictBusPack =  MapDictObject().mapDictObjectDBByIdoc(enabledPlaces)

        ## Mapear diccionarios para devolver al Front-end


        dictPlacesToInsert = MapperInserter.getDiccInsertions(dictBusPack,dictSait)


        localityToInsert = MapperDB().mapDestinosToLocalities(dictPlacesToInsert)

        db.closeConnection()

        ## PROCESO 4:
        ## Filtrar localities que no campos obligatorios provenientes de Sait.

        localityToInsertFiltered = [loc for loc in localityToInsert if loc.locality_name and loc.province_name and loc.idlocality and loc.isActive]
        
        return localityToInsertFiltered


   
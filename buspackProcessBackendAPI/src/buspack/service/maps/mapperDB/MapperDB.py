
from buspack.entities.enabled_placesDB.EnabledPlace import EnabledPlace
from buspack.entities.localityDB.Locality import Locality
from buspack.entities.zones_cp.zones_cp import zones_cp
from process.inserter.dtoInserterP1.DTOInserterP1 import DTOInserterP1
from process.inserter.dtoInserterP2.DTOInserterP2 import DTOInserterP2

class MapperDB():

    enabledPlaces = list()
    localities = list()

    keysEnabledPlaces = ['id', 'idog', 'isActive', 'code', 'place_name', 'type_description', 'locality_name', 'province_name']
    keysLocality = ['idlocality', 'zip_code', 'province_name', 'locality_name', 'enabled_place', 'isActive']

    @staticmethod
    def mapEnabledPlace(data):  ## Necesio que data sea una lista de diccionario con sus atributos, hace esa conversion en otro metodo aca.
        for elemento in data:
            dictElement = dict( zip( MapperDB.keysEnabledPlaces, elemento ) )
            enabledPlace = EnabledPlace(**dictElement)
            MapperDB.enabledPlaces.append(enabledPlace)
        return MapperDB.enabledPlaces

    @staticmethod
    def mapLocalities(data): ## data us dictionary
        
        if data != None:
            for elemento in data:
                dictElement = dict( zip( MapperDB.keysLocality, elemento ) )
                locality = Locality(**dictElement)
                MapperDB.localities.append(locality)
            return MapperDB.localities
        else:
            return None

    @staticmethod
    def mapDestinosToLocalities(data):
        localities = list()
        for idoc, destino in data.items():
            locality = DTOInserterP1(idoc, None, destino.Provincia, destino.Nombre, destino.Localidad, destino.Activo, destino.Codigo)
            localities.append(locality)
        return localities
    
    @staticmethod
    def mapJSONToDTOInserterP2(data):
        return  DTOInserterP2(
                idog = data.get('idog'),
                isActive = data.get('isActive'),
                code = data.get('code'),
                zone = data.get('zone'),
                zip_code = data.get('zip_code'),
                province_name = data.get('province_name'),
                locality_name = data.get('locality_name'),
                enabled_place = data.get('enabled_place'))


    @staticmethod
    def mapInserterP2ToLocality(tupleLocality):
        if tupleLocality == None:
            return  None
        else:
            return Locality(
                idlocality = None,
                zip_code = DTOInserterP2.zip_code,
                province_name = DTOInserterP2.province_name,
                locality_name = DTOInserterP2.locality_name,
                enabled_place = DTOInserterP2.enabled_place,
                isActive = DTOInserterP2.isActive)


    @staticmethod
    def mapDTOInserterP2ToLocality(DTOInserterP2):
        return Locality(
                idlocality = None,
                zip_code = DTOInserterP2.zip_code,
                province_name = DTOInserterP2.province_name,
                locality_name = DTOInserterP2.locality_name,
                enabled_place = DTOInserterP2.enabled_place,
                isActive = DTOInserterP2.isActive)

    @staticmethod
    def mapDTOInserterP2v2ToLocality(DTOInserterP2):
        if DTOInserterP2 == None:
            return None
        return Locality(
                idlocality = None,
                zip_code = DTOInserterP2[1],
                province_name = DTOInserterP2[2],
                locality_name = DTOInserterP2[3],
                enabled_place = DTOInserterP2[4],
                isActive = DTOInserterP2[5])

    @staticmethod
    def mapDTOInserterP2ToEnablePlace(DTOInserterP2):
        return EnabledPlace(
                id = None,
                idog = DTOInserterP2.idog,
                isActive = DTOInserterP2.isActive,
                code = DTOInserterP2.code,
                place_name = DTOInserterP2.enabled_place,
                type_description = "LOCALIDAD", 
                locality_name = DTOInserterP2.locality_name,
                province_name = DTOInserterP2.province_name)

    @staticmethod
    def mapDTOInserterP2ToZoneCP(DTOInserterP2):
            return zones_cp(
                id = None,
                cp = DTOInserterP2.zip_code,
                zone = DTOInserterP2.zone
            )

    @staticmethod
    def mapDTOInserterP2ToZoneCPToList(DTOInserterP2):
            return list(zones_cp(
                id = None,
                cp = DTOInserterP2.zip_code,
                zone = DTOInserterP2.zone
            ))

    @staticmethod
    def mapDTOInserterP2v2ToZoneCP(DTOInserterP2):
        if DTOInserterP2 == None:
            return None
        return zones_cp(
                id = None,
                cp = DTOInserterP2[1],
                zone = DTOInserterP2[2]
        )


    

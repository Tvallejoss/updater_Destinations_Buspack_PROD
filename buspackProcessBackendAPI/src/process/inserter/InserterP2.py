



from buspack.resources.db.DB import DB
from buspack.resources.repository.DBRepository import DBRepository
from buspack.service.maps.mapperDB.MapperDB import MapperDB
from excel.UpdateExcel import UpdateExcel


class InserterP2():

    @staticmethod
    def run(placeToInsert):


        ## PROCESO 2.0: Hidrato la lista de objeto provenientes de un JSON enviado por el Front-end

        DTOInserterP2 = MapperDB.mapJSONToDTOInserterP2(placeToInsert)    
        
        localityToDB = MapperDB.mapDTOInserterP2ToLocality(DTOInserterP2)

        enabled_placeToDB  = MapperDB.mapDTOInserterP2ToEnablePlace(DTOInserterP2) 

        zones_cpToDB = MapperDB.mapDTOInserterP2ToZoneCP(DTOInserterP2)

        
        ## PROCESO 2.1: Conectar a la Base de Datos

        db = DB()
        conexion = db.connect()

        ## PROCESO 2.2: Elimino localities y cp que ya estan en la BD -> Aca llegan Enables places que no estan en la BD, pero hay por error localities y cp asociados a este idoc de enabled places que fueron 
                                                                      ## insertados sin el enabled places, la BD no tiene relaciones por ende la comprobacion y mapeo es por nombre y numero de cp.

        

        mapperDB = MapperDB()


        localityDB = mapperDB.mapDTOInserterP2v2ToLocality(DBRepository().getLocalitiesByLocalityName(conexion,localityToDB.locality_name, localityToDB.enabled_place))
        
        zoneCpDB = mapperDB.mapDTOInserterP2v2ToZoneCP(DBRepository().getZonesCPByCP(conexion,int(zones_cpToDB.cp[0])))

        localityToDBFiltered = localityToDB if localityDB is None else None
        zone_cpToDBFiltered  = zones_cpToDB if zoneCpDB   is None else None

        print(zone_cpToDBFiltered)
        print("aaaaaaaaaa")
        print(localityToDBFiltered)
        ## PROCESO 2.3: inserto las listas a la Base de datos


        DBRepository.insertPlacesBDBuspack(conexion, enabled_placeToDB, zone_cpToDBFiltered , localityToDBFiltered)
        

        ## PROCESO 2.4 Cierro la conexion a la Base de datos

        db.closeConnection()
        

        return("Insercion realizada correctamente")


    """

    for idoc, object in dictPlacesToInsert.items():
        print(idoc)

            ## Actualizo Base de Datos Produccion de Buspack

            # DBRepository.updateEnabledPlaces(conexion, dictBusPack_updated)

            # Cerrar conexion a Base de Datos

    db.closeConnection()

    """

    UpdateExcel.run()
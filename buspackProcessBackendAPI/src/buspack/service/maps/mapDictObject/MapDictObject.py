

class MapDictObject():

    @staticmethod
    def mapDictObjectSaitByIdoc(listObject):
        dicc = dict()
        for object in listObject:
            dicc[object.IDOG] = object
        return dicc
    
    @staticmethod
    def mapDictObjectDBByIdoc(listObject):
        dicc = dict()
        for object in listObject:
            dicc[object.idog] = object
        return dicc
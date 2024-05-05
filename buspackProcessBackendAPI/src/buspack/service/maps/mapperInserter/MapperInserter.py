
class  MapperInserter():    

    @staticmethod
    def getDiccInsertions(dictBDBuspack, dictSait):  
        dictToInsert = dict()
        for idoc, objectSait in dictSait.items():                              
            if idoc not in dictBDBuspack:
             dictToInsert[idoc] = objectSait
        return dictToInsert

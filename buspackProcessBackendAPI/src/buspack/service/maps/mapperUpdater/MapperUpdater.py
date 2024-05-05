
class  MapperUpdater():    
    @staticmethod
    def updateDictBD(dictToUpdate, dictUpdated):  
        for idoc, objectSait in dictUpdated.items():                              
            if idoc in dictToUpdate:
             dictToUpdate[idoc].isActive = objectSait.Activo
        return dictToUpdate
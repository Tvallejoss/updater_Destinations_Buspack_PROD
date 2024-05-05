
class EnabledPlace():
    def __init__(self, id, idog, isActive, code, place_name, type_description, locality_name, province_name):
        self.id = id
        self.idog = idog
        self.isActive = isActive
        self.code = code
        self.place_name = place_name
        self.type_description = type_description
        self.locality_name = locality_name
        self.province_name = province_name
    
    def isActivo(enabledPlace):
            return (enabledPlace.isActive == "1")
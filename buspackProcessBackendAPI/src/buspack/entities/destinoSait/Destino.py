
class Destino():
        def __init__(self, IDOG, Activo, Codigo, Nombre, DescTipo, Localidad, Provincia):
            self.IDOG = IDOG
            self.Activo = Activo
            self.Codigo = Codigo
            self.Nombre = Nombre
            self.DescTipo = DescTipo
            self.Localidad = Localidad
            self.Provincia = Provincia
        
        def isTipoLocalidad(destino):
            return (destino.DescTipo == "Localidad           ") ## Viene con dicho espacio de Sait, no eliminar, hay que respetarlo.
        
        def isActivo(destino):
            return (destino.Activo == "1")
        
        def changeDescTipoToLocalidad(destino):
            destino.DescTipo = "Localidad           "
            return destino
from buspack.entities.destinoSait.Destino import Destino

class MapperDestino():
    destinos = []
    @staticmethod
    def mapDestinations(data):
        for elemento in data:
            destino = Destino(**elemento)
            MapperDestino.destinos.append(destino)
        return MapperDestino.destinos


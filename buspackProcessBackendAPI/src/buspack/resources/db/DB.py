
import mysql.connector

class DB():


    def __init__(self):
        self.host = "192.168.156.131"
        self.user = "it-soporte"
        self.password = "Telefono4528*"
        self.database = "backendnest"
        self.conexion = None

    def connect(self):
        try:
            conexion = mysql.connector.connect(
                host = self.host,
                user= self.user,
                password = self.password,
                database = self.database
            )
            if conexion.is_connected():
                print("Conexión exitosa a la base de datos")
                self.conexion = conexion
                return conexion
            else:
                print("No se pudo conectar a la base de datos")
                exit()
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos: ", error, "Recuerde que debe tener la VPN activa")
            exit()
        
    def closeConnection(self):
        if 'conexion' in locals() and self.conexion.is_connected():
            self.conexion.close()
        print("Conexión a Base de Datos cerrada con exito")
    

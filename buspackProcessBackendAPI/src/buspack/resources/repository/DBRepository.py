
import base64
from io import BytesIO


class DBRepository():

    @staticmethod
    def getEnabledPlaces(conexion):
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM enabled_places")  
        resultados = cursor.fetchall()
        return resultados

    @staticmethod
    def getLocalities(conexion):
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM locality")  
        resultados = cursor.fetchall()
        return resultados

    @staticmethod
    def getLocalitiesByLocalityName(conexion, name, namePlace):
        cursor = conexion.cursor()
        query = "SELECT * FROM locality WHERE locality_name LIKE %s AND enabled_place LIKE %s LIMIT 1"
        cursor.execute(query, ('%' + name + '%', '%' + namePlace + '%')) 
        resultados = cursor.fetchone()
        if resultados == None:  # Si la lista de resultados está vacía
            return None  
        return resultados  
        

    @staticmethod
    def getZonesCPByCP(conexion, cp):
        cursor = conexion.cursor()
        query = "SELECT * FROM zones_cp WHERE cp = %s LIMIT 1"
        cp_str = str(cp)
        cursor.execute(query, (cp_str,))
        resultados = cursor.fetchone()
        if resultados == None:  # Si la lista de resultados está vacía
            return None 
        return resultados
        
    
    @staticmethod
    def getExcel(conexion):
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM planilla_excel")  
        resultado = cursor.fetchone()
        return resultado

    def updateEnabledPlaces(conexion,dictBusPack):
        try:
            for id, objeto in dictBusPack.items():
                # Genera la consulta SQL UPDATE utilizando los atributos del objeto
                consulta = f"UPDATE enabled_places SET "
                for atributo, valor in objeto.__dict__.items():
                    # Aquí asumimos que los atributos del objeto coinciden con los nombres de las columnas en la tabla
                    if atributo != 'id':  # Excluimos el atributo 'id'
                        consulta += f"{atributo} = '{valor}', "
                # Elimina la coma extra al final y agrega la condición WHERE
                consulta = consulta[:-2] + f" WHERE id = {id};"
                
                # Ejecuta la consulta
                conexion.cursor().execute(consulta)

            # Realiza commit para confirmar los cambios en la base de datos
            conexion.commit()
            print("Actualización exitosa")

        except Exception as e:
            print(f"Error durante el UPDATE en la Base de Datos. Se procede a realizar un ROLLBACK. : {str(e)}")
            # En caso de error, realiza rollback para deshacer los cambios
            conexion.rollback()
    
    def insertPlacesBDBuspackWithDicctionay(conexion, enabled_places, zones_cps, localities):
        try:

            ## inserto enabledplaces

            for objeto in enabled_places:
                # Genera la consulta SQL INSERT utilizando los atributos del objeto
                consulta = f"INSERT INTO enabled_places ("
                
                # Obtiene los nombres de los atributos del objeto
                atributos = ', '.join(objeto.__dict__.keys())
                consulta += atributos + ") VALUES ("
                
                # Obtiene los valores de los atributos del objeto y los formatea adecuadamente
                valores = "', '".join(map(str, objeto.__dict__.values()))
                consulta += f"'{valores}');"
                
                # Ejecuta la consulta
                conexion.cursor().execute(consulta)
            
            # Realiza commit para confirmar los cambios en la base de datos
            conexion.commit()
            print("Inserción EnabledPlaces exitosa")

            
            ## inserto zones_cp 

            for objeto in zones_cps:
                # Genera la consulta SQL INSERT utilizando los atributos del objeto
                consulta = f"INSERT INTO zones_cp ("
                
                # Obtiene los nombres de los atributos del objeto
                atributos = ', '.join(objeto.__dict__.keys())
                consulta += atributos + ") VALUES ("
                
                # Obtiene los valores de los atributos del objeto y los formatea adecuadamente
                valores = "', '".join(map(str, objeto.__dict__.values()))
                consulta += f"'{valores}');"
                
                # Ejecuta la consulta
                conexion.cursor().execute(consulta)
            
            # Realiza commit para confirmar los cambios en la base de datos
            conexion.commit()
            print("Inserción exitosa")


            ## inserto locality 

            for objeto in localities:
                # Genera la consulta SQL INSERT utilizando los atributos del objeto
                consulta = f"INSERT INTO locality ("
                
                # Obtiene los nombres de los atributos del objeto
                atributos = ', '.join(objeto.__dict__.keys())
                consulta += atributos + ") VALUES ("
                
                # Obtiene los valores de los atributos del objeto y los formatea adecuadamente
                valores = "', '".join(map(str, objeto.__dict__.values()))
                consulta += f"'{valores}');"
                
                # Ejecuta la consulta
                conexion.cursor().execute(consulta)
            
            # Realiza commit para confirmar los cambios en la base de datos
            conexion.commit()
            print("Inserción exitosa")
        
        except Exception as e:
            print(f"Error durante EL INSERT en la Base de Datos. Se procede a realizar un ROLLBACK. : {str(e)}")
            # En caso de error, realiza rollback para deshacer los cambios
            conexion.rollback()

    
    def insertPlacesBDBuspack(conexion, enabled_place, zone_cp, locality):
        
        try:

            if locality != None and zone_cp != None:
                cp_value = getattr(locality, 'zip_code')
                print(cp_value)
                zone_value = getattr(zone_cp, 'zone')
                consulta = f"INSERT INTO zones_cp (cp, zone) VALUES ('{cp_value}', '{zone_value}');"
                print(consulta)
                conexion.cursor().execute(consulta)


            # Insertar locality
            if locality != None:
                consulta = f"INSERT INTO locality (zip_code, province_name, locality_name, enabled_place, isActive) VALUES ("
                valores = "', '".join(str(getattr(locality, attr)) for attr in ['zip_code', 'province_name', 'locality_name', 'enabled_place', 'isActive'])
                consulta += f"'{valores}');"
                conexion.cursor().execute(consulta)


            # Insertar enabled_place
            consulta = f"INSERT INTO enabled_places (idog, isActive, code, place_name, type_description, locality_name, province_name) VALUES ("
            valores = "', '".join(str(getattr(enabled_place, attr)) for attr in ['idog', 'isActive', 'code', 'place_name', 'type_description', 'locality_name', 'province_name'])
            consulta += f"'{valores}');"
            conexion.cursor().execute(consulta)


            # Realizar commit para confirmar los cambios en la base de datos
            conexion.commit()
            print("Inserción exitosa")

        except Exception as e:
            print(f"Error durante el INSERT en la Base de Datos. Se procede a realizar un ROLLBACK: {str(e)}")
            # En caso de error, realizar rollback para deshacer los cambios
            conexion.rollback()


    def updateExcel(conexion,excel):
        try:

            # Genera la consulta SQL UPDATE utilizando los atributos del objeto
            consulta = f"UPDATE planilla_excel SET "
            consulta += f"excel = '{excel}'"
            # Elimina la coma extra al final y agrega la condición WHERE
            consulta += f" WHERE id = 2;"
            cursor = conexion.cursor()
            # Ejecuta la consulta
            cursor.execute(consulta)

            # Realiza commit para confirmar los cambios en la base de datos
            conexion.commit()
            print("Actualización exitosa")

        except Exception as e:
            print(f"Error durante el UPDATE en la Base de Datos. Se procede a realizar un ROLLBACK. : {str(e)}")
            # En caso de error, realiza rollback para deshacer los cambios
            conexion.rollback()



    
    
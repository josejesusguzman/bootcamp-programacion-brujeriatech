import psycopg2
from configparser import ConfigParser

def leer_config(archivo="postgresql.ini", seccion='postgresql'):
    parser = ConfigParser()
    parser.read(archivo)
    bd = {}
    if parser.has_section(seccion):
        params = parser.items(seccion)
        for param in params:
            bd[param[0]] = param[1]

    return bd

def conectar():
    conexion = None
    try:
        params = leer_config()
        print(params)
        print("Conectando...")
        conexion = psycopg2.connect(**params)
        cursor = conexion.cursor()

        cursor.execute("SELECT version()")
        version = cursor.fetchone()
        print(version)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conexion is not None:
            conexion.close()
            print("Conexión finalizada")

conectar()
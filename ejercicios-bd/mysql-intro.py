import mysql.connector
from mysql.connector import errorcode

# SSL: https://cacerts.digicert.com/DigiCertGlobalRootG2.crt.pem

config = {
    'host' :"mibase123456789.mysql.database.azure.com",
    'user' : "jesus",
    'password': "5f6g7h8j9k0l.-",
    'database': 'mibasededatos'#,
    #'client_flags': [mysql.connector.ClientFlag.SSL],
    #'ssl_ca': '\DigiCertGlobalRootG2.crt.pem'
}

try :
    conn = mysql.connector.connect(**config)
    print("Conexión establecida")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_DBACCESS_DENIED_ERROR:
        print("No tienes permiso de estar aquí. Perro 🐕")
    elif err.errno == errorcode.ER_BAD_DB_ERROR: 
        print("La base de datos no existe")
    else:
        print(err)
else:
    mi_cursor = conn.cursor()

mi_cursor.execute("DROP TABLE IF EXISTS inventario;")
print("Eliminamos la tabla inventario")

mi_cursor.execute("CREATE TABLE inventario (id serial PRIMARY KEY, producto VARCHAR(50), cantidad int);")
print("Creamos la tabla inventario")

mi_cursor.execute("INSERT INTO inventario (producto, cantidad) VALUES ('Laptop DELL', 5);")
print("Insertados ", mi_cursor.rowcount, " registros de datos")

mi_cursor.execute("INSERT INTO inventario (producto, cantidad) VALUES ('Laptop Huawei', 35);")
print("Insertados ", mi_cursor.rowcount, " registros de datos")

mi_cursor.execute("INSERT INTO inventario (producto, cantidad) VALUES ('Laptop Lenovo', 10);")
print("Insertados ", mi_cursor.rowcount, " registros de datos")

mi_cursor.execute("INSERT INTO inventario (producto, cantidad) VALUES ('Macbook', 0);")
print("Insertados ", mi_cursor.rowcount, " registros de datos")

# Leer los datos
mi_cursor.execute("SELECT * FROM inventario;")
registros = mi_cursor.fetchall()
print("Leidos", mi_cursor.rowcount, "registros de datos")

for row in registros:
    print("Quedan", str(row[2]), str(row[1]))

# Actualizar registro
mi_cursor.execute("UPDATE inventario SET cantidad = %s, producto= %s WHERE producto=%s;", (10, "Laptop Chayomi", 'Laptop DELL'))
print("Actualizados ", mi_cursor.rowcount, " registros de datos")
mi_cursor.execute("UPDATE inventario SET cantidad = %s WHERE producto= %s;", (10, "Macbook"))
print("Actualizados ", mi_cursor.rowcount, " registros de datos")

print("---------------------------------------------")

# Leer los datos
mi_cursor.execute("SELECT * FROM inventario;")
registros = mi_cursor.fetchall()
print("Leidos", mi_cursor.rowcount, "registros de datos")

for row in registros:
    print("Quedan", str(row[2]), str(row[1]))

print("---------------------------------------------")
#Eliminar datos
mi_cursor.execute("DELETE FROM inventario WHERE producto=%(param1)s;", {'param1': "Macbook"})
print("Eliminados ", mi_cursor.rowcount, " registros de datos")

print("---------------------------------------------")

# Leer los datos
mi_cursor.execute("SELECT * FROM inventario;")
registros = mi_cursor.fetchall()
print("Leidos", mi_cursor.rowcount, "registros de datos")

for row in registros:
    print("Quedan", str(row[2]), str(row[1]))
    
print("---------------------------------------------")

# Después de todas las consultas que haya hecho tu programa
# Tienes que hacer la limpieza
conn.commit()
mi_cursor.close()
conn.close()
print("Ya acabe 🥵")
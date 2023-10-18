from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['mibasededatos']

# Aquí se llaman colecciones pero podríamos decir que son las tablas de Mongo
collection = db['micoleccion']

# Create - Read - Update - Delete

# Create
collection.insert_one({
    "nombre": "Jesus",
    "edad": 28,
    "telefono": "5521527721",
    "correo": "correo@correo.mx"
})

#Read
for document in collection.find() :
    print(document)

print("---------------------------------")

# Create
collection.insert_one({
    "nombre": "Mari",
    "direccion": {
        "calle": "Benito Camelo",
        "numero_exterior": "69",
        "numero_inteior": "96",
        "colonia": "rosa",
        "localidad": "mesta",
        "ciudad": "larga",
        "estado": "Tamaulipas"
    },
    "hijos": {
        "hijo1": {
            "nombre": "Zara",
            "apellido": "Goza de alegria",
            "edad": 23
        },
        "hijo2": {
            "nombre": "Elver",
            "apellido": "Galarga",
            "edad": 18
        }
    }
})

# Update
collection.update_one({"nombre": "Jesus"}, {"$set": {"telefono": "0000000000"}})

# Read
for document in collection.find() :
    print(document)

print("---------------------------------")

# Delete
collection.delete_one({"nombre": "Jesus"})

# Read
for document in collection.find() :
    print(document)
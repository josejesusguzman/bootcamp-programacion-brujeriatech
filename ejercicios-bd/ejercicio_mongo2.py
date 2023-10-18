from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['mibasededatos']

collection = db['usuarios']

usuarios = [
    {"nombre": "arvo", "edad": 11, "direccion": {"ciudad": "Tepito", "estado": "CDMX"}},
    {"nombre": "Angel", "edad": 23, "direccion": {"ciudad": "Toluca", "estado": "Estado de México"}},
    {"nombre": "Alvaro", "edad": 36, "direccion": {"ciudad": "Merida", "estado": "Yucatán"}}
]

collection.insert_many(usuarios)

users_36_years = collection.find({"edad": 36})

for user in users_36_years :
    print(user)

pipeline = [
    {"$group": { "_id": None, "promedio_edad": { "$avg": "$edad" }}}
]

promedio_edad = collection.aggregate(pipeline)

for resultado in promedio_edad:
    print(resultado)
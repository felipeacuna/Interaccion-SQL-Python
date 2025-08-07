import pymongo
import requests

# Generar un nuevo cliente
client = pymongo.MongoClient("mongodb://localhost:27017/")
print('Conexion exitosa')

mydb = client['feriados']
print('Conexión a la db exitosa')

col = mydb['feriados2024']
print('Conexión a la colección exitosa')

# Eliminar todos los documentos
col.delete_many({})

# Extraer la información de la API
# request a la API
# POST, PUT, PATCH, DELETE, GET
response = requests.get('https://apis.digital.gob.cl/fl/feriados/2024', headers={
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
})

#print(response.json())

# Insertar lista de documentos
docs = response.json()
col.insert_many(docs)
print('Documentos insertados')

# 4.A- Obtener todos los feriados en la colección

print('\n=============4.a- Feriados 2024=============')
consultaa = col.find({}, {'_id':0})
for r in consultaa:
    print(r)

# 4.B- Obtener todos los feriados de tipo religioso

print('\n=============4.b- Feriados 2024 de tipo religioso=============')
consultab = col.find({'tipo':'Religioso'}, {'_id':0})
for r in consultab:
    print(r)

# 4.C- Obtener solo los feriados irrenunciables
print('\n=============4.c- Feriados 2024 irrenunciables=============')
consultac = col.find({'irrenunciable':'1'}, {'_id':0})
for r in consultac:
    print(r)

# 4.D- Obtener los feriados que incluyen el texto "Santo" en su nombre
print('\n=============4.D- Feriados 2024 con la palabra "Santo"=============')
consultad =col.find({'nombre':{"$regex": 'Santo'}}, {'_id':0})
for r in consultad:
    print(r)

# 4.E- Obtener solo los feriados que se celebran entre el 11 de marzo y el 31 de agosto
print('\n=============4.E- Feriados 2024 entre el 11 de marzo y el 31 de agosto=============')
consultae = col.find({'fecha': {'$gte': '2024-03-11', '$lte': '2024-08-31'}}, {'_id':0})
for r in consultae:
    print(r)

# 5- Insertar un nuevo feriado
feriadonuevo = { 'nombre': 'Día de las luces', 'comentarios': 'null', 'fecha': '2024-03-11', 'irrenunciable':'0', 'tipo': 'Religioso'}
col.insert_one(feriadonuevo)
print('\n=============5- Feriado agregado=============')

vernuevoferiado = col.find_one({'nombre':'Día de las luces'})
print(vernuevoferiado)
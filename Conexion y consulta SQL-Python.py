# 4. Conectarse al esquema mp1
import mysql. connector as db

mydb = db.connect(
    host='localhost',
    user='root',
    password='mysql123',
    database= 'mp1'
)

# 5.a- Obtener la información de la sociedad con rut 77886308-1
cursor = mydb.cursor()
sqlSentence1 = 'SELECT * from sociedades WHERE rut = "77886308-1"'
cursor.execute(sqlSentence1)
rows = cursor.fetchall()
print("5.a: Información de la sociedad con rut 77886308-1:")
for row in rows:
   print(row)

# 5.b- Obtener todas las sociedades cuyo capital es mayor o igual a $400.000.000 (400 millones de pesos)
cursor = mydb.cursor()
sqlSentence2 = 'SELECT * from sociedades WHERE capital >= 400000000'
cursor.execute(sqlSentence2)
rows = cursor.fetchall()
print("5.b: Sociedades con capital mayor a 400 millones de pesos:")
for row in rows:
    print(row[2])

# 6- Desde el programa, insertar una nueva sociedad a la tabla

cursor = mydb.cursor()
sqlSentence3 = 'INSERT INTO sociedades (id, rut, nombre, registro, comuna, capital) VALUES (%s, %s, %s, %s, %s, %s)'
sociedad = (5156305, '77721389-k','Estrellas SpA','2024-03-11','PROVIDENCIA',1000000)
cursor.execute(sqlSentence3,sociedad)
mydb.commit()
print("6. Se ha agregado una nueva sociedad con la siguiente información:","\n",sociedad)

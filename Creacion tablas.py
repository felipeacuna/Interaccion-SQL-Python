# Importar librerías necesarias. NO SE DEBE IMPORTAR NINGUNA OTRA LIBRERÍA.
import mysql. connector as db
import csv

# Desde este punto en adelante se debe crear el código pedido.

mydb = db.connect(
    host='localhost',
    user='root',
    password='mysql123',
    database= 'mp2'
)

cursor = mydb.cursor()

# 0. Borrar tablas

borrar_productos_pedidos = 'DROP TABLE IF EXISTS productos_pedidos'
cursor.execute(borrar_productos_pedidos)

borrar_productos = 'DROP TABLE IF EXISTS productos'
cursor.execute(borrar_productos)

borrar_pedidos = 'DROP TABLE IF EXISTS pedidos'
cursor.execute(borrar_pedidos)

borrar_clientes = 'DROP TABLE IF EXISTS clientes'
cursor.execute(borrar_clientes)



#2.1 Creación de tabla productos
crear_productos = '''
CREATE TABLE productos (
id INT PRIMARY KEY,
nombre VARCHAR(255),
descripcion VARCHAR(255),
precio INT
)
'''
cursor.execute(crear_productos)

#2.2 Creación de tabla clientes
crear_clientes = '''
CREATE TABLE clientes (
id INT PRIMARY KEY,
nombre VARCHAR(255),
email VARCHAR(255)
)
'''
cursor.execute(crear_clientes)

#2.3 Creación de tabla pedidos
crear_pedidos = '''
CREATE TABLE pedidos (
id INT PRIMARY KEY,
fecha DATE,
direccion VARCHAR(255),
id_cliente INT,
detalle VARCHAR(255),
FOREIGN KEY (id_cliente) REFERENCES clientes(id)
)
'''
cursor.execute(crear_pedidos)

#2.4 Creación de tabla productos_pedidos
crear_productos_pedidos = '''
CREATE TABLE productos_pedidos (
id_producto INT,
id_pedido INT,
cantidad INT,
PRIMARY KEY (id_producto, id_pedido),
FOREIGN KEY (id_producto) REFERENCES productos(id),
FOREIGN KEY (id_pedido) REFERENCES pedidos(id)
)
'''
cursor.execute(crear_productos_pedidos)

# 3.1 Carga de datos de clientes
with open('data/clientes.csv', 'r') as file:
    CSVReader = csv.reader(file, delimiter=',')
    next(CSVReader)
    filas_clientes = []
    for cliente in CSVReader:
        filas_clientes.append(cliente)

insertar_clientes = 'INSERT INTO clientes (id, nombre, email) VALUES (%s, %s, %s)'
cursor.executemany(insertar_clientes, filas_clientes)
mydb.commit()

# 3.2 Carga de  datos de pedido
with open('data/pedidos.csv', 'r') as file:
    CSVReader = csv.reader(file, delimiter=',')
    next(CSVReader)
    filas_pedidos = []
    for pedido in CSVReader:
        filas_pedidos.append(pedido)

insertar_pedidos = 'INSERT INTO pedidos (id, fecha, direccion, id_cliente, detalle) VALUES (%s, %s, %s, %s, %s)'
cursor.executemany(insertar_pedidos, filas_pedidos)
mydb.commit()

#3.3 Carga de datos de productos
with open('data/productos.csv','r') as file:
    CSVReader = csv.reader(file, delimiter=',')
    next(CSVReader)
    filas_productos = []
    for producto in CSVReader:
        filas_productos.append(producto)

insertar_productos = 'INSERT INTO productos (id, nombre, descripcion, precio) VALUES (%s, %s, %s, %s)'
cursor.executemany(insertar_productos, filas_productos)
mydb.commit()

#3.4 Carga de datos de productos_pedidos
with open('data/productos_pedidos.csv', 'r') as file:
    CSVReader = csv.reader(file, delimiter=',')
    next(CSVReader)
    filas_productos_pedidos = []
    for productos_pedido in CSVReader:
        filas_productos_pedidos.append(productos_pedido)

insertar_productos_pedidos = 'INSERT INTO productos_pedidos (id_producto, id_pedido, cantidad) VALUES (%s, %s, %s)'
cursor.executemany(insertar_productos_pedidos, filas_productos_pedidos)
mydb.commit()
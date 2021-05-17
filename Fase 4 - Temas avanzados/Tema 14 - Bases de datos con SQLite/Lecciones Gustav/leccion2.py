import sqlite3

# conexion = sqlite3.connect("usuarios.db")
# conexion = sqlite3.connect("productos.db")
conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

# cursor.execute('''
#     CREATE TABLE usuarios(
#         dni VARCHAR(9) PRIMARY KEY,
#         nombre VARCHAR(100),
#         edad INTEGER,
#         email VARCHAR(100)
#     )
# ''')

# usuarios = [
#     ('1a','Gustav',29,'rungustavo@gmail.com'),
#     ('1b','Mario',51,'mario@ejemplo.com'),
#     ('1c','Mercedez',38,'maria@ejemplo.com'),
#     ('1d','Juan',19,'juan@ejemplo.com'),
# ]

# cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)

# cursor.execute("INSERT INTO usuarios VALUES ('1e','Juan',19,'juan@ejemplo.com')")

# cursor.execute('''
#     CREATE TABLE productos (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         nombre VARCHAR(100) NOT NULL,
#         marcha VARCHAR(50) NOT NULL,
#         precio FLOAT NOT NULL
#     )
# ''')

# productos = [
#     ('Teclado','Logitech',19.95),
#     ('Pantalla','LG',89.95)
# ]

# cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)

# cursor.execute("SELECT * FROM productos")
# productos = cursor.fetchall()
# for i in productos:
#     print(i)

# cursor.execute('''
#     CREATE TABLE usuarios(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         dni VARCHAR(9) UNIQUE,
#         nombre VARCHAR(100),
#         edad INTEGER,
#         email VARCHAR(100)
#     )
# ''')

# usuarios = [
#     ('1a','Gustav',29,'rungustavo@gmail.com'),
#     ('1b','Mario',51,'mario@ejemplo.com'),
#     ('1c','Mercedez',38,'maria@ejemplo.com'),
#     ('1d','Juan',19,'juan@ejemplo.com'),
# ]

# cursor.executemany("INSERT INTO usuarios VALUES (null,?,?,?,?)", usuarios)

cursor.execute("INSERT INTO usuarios VALUES (null,'1e','Juan',19,'juan@ejemplo.com')")

conexion.commit()
conexion.close()
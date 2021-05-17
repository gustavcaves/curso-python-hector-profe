import sqlite3

conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor()

# cursor.execute("CREATE TABLE usuario (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

# cursor.execute("INSERT INTO usuario VALUES ('Gustav','29','rungustavo@gmail.com')")

# cursor.execute("SELECT * FROM usuario")
# usuario = cursor.fetchone()
# print(usuario[1])

# usuarios = [
#     ('Mario',51,'mario@ejemplo.com'),
#     ('Mercedez',38,'maria@ejemplo.com'),
#     ('Juan',19,'juan@ejemplo.com'),
# ]
# cursor.executemany("INSERT INTO usuario VALUES (?,?,?)", usuarios)

cursor.execute("SELECT * FROM usuario")

usuarios = cursor.fetchall()

print(usuarios)

for i in usuarios:
    print("Nombre: ",i[0],"\tEmail: ",i[2])

conexion.commit()
conexion.close()
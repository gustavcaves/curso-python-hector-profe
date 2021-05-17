import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

# cursor.execute("SELECT * FROM usuarios WHERE edad=29")

# usuario = cursor.fetchall()
# print(usuario)

# cursor.execute("UPDATE usuarios SET nombre='Gustav Caves', edad=30 WHERE dni='1a'")

# cursor.execute("DELETE FROM usuarios WHERE dni='1e'")

cursor.execute("DELETE FROM usuarios")

conexion.commit()
conexion.close()
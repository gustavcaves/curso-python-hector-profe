import sqlite3
from tkinter import *

# Configuramos la raiz
root = Tk()
root.title("Bar Don Caves - Menú")
root.resizable(1,1)
root.config(bd=25, relief="ridge")

Label(root, text="Bar Don Caves", fg="blue", font=('Georgia',28,'bold')).pack()
Label(root, text="Menú del día", fg="orange", font=("Georgia",24,'bold')).pack()

# Separacion de titulos y categorias
Label(root, text="").pack()

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

# Buscar las categorias y platos de la bd

categorias = cursor.execute("SELECT * FROM categoria").fetchall()
for i in categorias:
    Label(root, text=i[1], fg="red", font=('Georgia',20,'bold')).pack()
    platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(i[0])).fetchall()
    for x in platos:
        Label(root, text=x[1], fg="gray", font=('Georgia',15,'italic')).pack()

    # Separacion de titulos y categorias
    Label(root, text="").pack()

conexion.close()

# Precio del meni
Label(root, text="21 EUR (IVA incl.)", fg="purple", font=('Georgia',20,'bold')).pack(side="left")

# Finalmene ejecutamos el bucle
root.mainloop()
import sqlite3

def crear_db():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    try:
        cursor.execute('''
        CREATE TABLE categoria(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) UNIQUE NOT NULL)
        ''')
    except sqlite3.OperationalError:
        print("La tabla categorias ya existe")
    else:
        print("La tabla categorias se ha creao correctamente.")

    try:
        cursor.execute('''
        CREATE TABLE plato(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) UNIQUE NOT NULL, 
            categoria_id INTEGER NOT NULL,
            FOREIGN KEY(categoria_id) REFERENCES categoria(id))
        ''')
    except sqlite3.OperationalError:
        print("La tabla platos ya existe")
    else:
        print("La tabla platos se ha creao correctamente")

    conexion.close()

def agregar_categoria():
    categoria = input("¿Nombre de la nueva categoría?\n")

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format(categoria))
    except sqlite3.IntegrityError:
        print("La categoría {} ya existe".format(categoria))
    else:
        print("La categoría {} se ha creado correctamente".format(categoria))

    conexion.commit()
    conexion.close()

def agregar_plato():

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    print("Selecciona una categoría para añadir el plato: ")
    for i in categorias:
        print("[{}] {}".format(i[0],i[1]))

    categoria_usuario = int(input("> "))

    plato = input("¿Nombre del nuevo plato?\n> ")

    try:
        cursor.execute("INSERT INTO plato VALUES (null, '{}', {})".format(plato, categoria_usuario))
    except sqlite3.IntegrityError:
        print("El plato {} ya existe".format(plato))
    else:
        print("El Plato {} se ha creado correctamente".format(plato))

    conexion.commit()
    conexion.close()


def mostrar_menu():
    
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    for i in categorias:
        print(i[1])
        platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(i[0])).fetchall()
        for x in platos:
            print("\t{}".format(x[1]))

    conexion.commit()
    conexion.close()

# Crear la base de datos en primera instancia
crear_db()

# Menu de opciones del programa
while True:
    print("Bienvenido al gestor del restaurante!")
    opcion = input("\nIntroduce una opción:\n[1] Agregar una categoría\n[2] Agregar un plato\n[3] Mostrar Menú\n[4] Salir del programa\n\n")

    if opcion == "1":
        agregar_categoria()
    elif opcion == "2":
        agregar_plato()
    elif opcion == "3":
        mostrar_menu()
    elif opcion == "4":
        print("Nos vemos!")
        break
    else:
        print("Opcion Incorrecta")
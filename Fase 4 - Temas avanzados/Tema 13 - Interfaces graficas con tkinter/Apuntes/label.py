from tkinter import *

# Configuración de la raíz
root = Tk()

# Variables dinámicas
texto = StringVar()
texto.set("This is\nGustav Caves\nCome on let´s take a walk")

pl = Label(root, text="¡Hello World!")
pl.pack(anchor="center")
label = Label(root, text="¡Otra etiqueta!")
label.pack(anchor="center")
pl2 = Label(root, text="¡That´s cute!")
pl2.pack(anchor="center")


pl.config(bg="blue", fg="white", font=("Georgia", 48))
label.config(bg="yellow", fg="black", font=("Noto Serif",24))
label.config(textvariable=texto)
pl2.config(bg="blue", fg="white", font=("Georgia", 48))



imagen = PhotoImage(file="CursoPython\Fase 4 - Temas avanzados\Tema 13 - Interfaces graficas con tkinter\Apuntes\imagen.gif")
Label(root, image=imagen, bd=0).pack(anchor="center")

# Finalmente bucle de la apliación
root.mainloop()
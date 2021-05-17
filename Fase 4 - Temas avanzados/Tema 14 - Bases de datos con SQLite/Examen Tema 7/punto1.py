from tkinter import *

root = Tk()
root.title("Aplicación grafica en python")
label = Label(root, text="Hola Mundo!!!")
label.pack()
label.config(fg="orange", bg="white", font=("Georgia",42))
Button(root, text="OK!!!").pack()

root.mainloop()
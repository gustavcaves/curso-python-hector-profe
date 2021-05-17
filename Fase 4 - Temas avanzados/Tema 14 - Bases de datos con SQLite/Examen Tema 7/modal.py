from tkinter import *

root = Tk()
root.title("Aplicación grafica en python")
label = Label(root, text="Pulsa OK!!! Para Abrir Ventana Modal")
label.pack()
label.config(fg="orange", bg="white", font=("Georgia",42))

def vmodal():

    vm = Toplevel(root)
    vm.grab_set()
    vm.title("Ventana Modal")
    Label(vm, text='Ahora haz clic en el boton para cerrar --------------> :)').pack()
    Button(vm,text="Cerrar", command=vm.destroy).pack()

Button(root, text="OK!!!", command=vmodal).pack()

root.mainloop()
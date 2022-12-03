from tkinter import *

root=Tk()
root.title('Pies a Metros')
root.geometry('200x100')

e=StringVar()
e=Entry(root, width=10)
e.grid(row=0, column=1)

def convertir(*args): #para que se active con el ENTER debo indicar que tome los argumentos '*args'
    try:
        value=float(e.get())  #pasar lo ingresado a tipo float para poder realizar operaciones matemáticas
        resultado=float(value*0.3048)
        textvariable.set(resultado)
    except ValueError:
        textvariable.set('Error')
    e.delete(0,END)

btn=Button(root, text='Calcular', command=convertir)
btn.grid(row=2, column=2)

textvariable=StringVar()
      
l1=Label(root, text='          ')
l3=Label(root, text='Pies')
l4=Label(root, text='Es igual a')
l5=Label(root, textvariable=textvariable)
l6=Label(root, text='Metros')
l7=Label(root, text='          ')
l8=Label(root, text='          ')

l1.grid(row=0, column=0)
l3.grid(row=0, column=2)
l4.grid(row=1, column=0)
l5.grid(row=1, column=1)
l6.grid(row=1, column=2)
l7.grid(row=2, column=0)
l8.grid(row=2, column=1)

e.focus() #Cuando se abre la app, el cursor empieza en la barra de input 'e'
root.bind('<Return>', convertir)  #Activa la funcion 'convertir' al dar ENTER
root.mainloop()

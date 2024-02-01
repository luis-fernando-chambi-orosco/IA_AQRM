import cv2
import seguimientomanos as sm
from tkinter import *
from PIL import Image, ImageTk
#interfaz 
mano_abierta = True  # Suponemos que la mano está abierta al inicio
conteo_repeticiones = 0
detector = sm.detectormanos(Confdeteccion=int(0.75))

cap = cv2.VideoCapture(0)
def umbral():
    while True:
        global mano_abierta,conteo_repeticiones
        ret, frame = cap.read()
        frame = detector.encontrarmanos(frame)

        # Verificar el estado actual de la mano
        manos_info, cuadro = detector.encontrarposicion(frame, dibujar=False)
        if len(manos_info) != 0:
            dedos = detector.dedosarriba()
            #print(dedos)
            if dedos.count(0)>=2 and mano_abierta:
                mano_abierta = False
                conteo_repeticiones += 1
                print("Conteo de repeticiones:", conteo_repeticiones)
            elif all(dedos) and not mano_abierta:
                # Todos los dedos estaban bajados y ahora están arriba
                mano_abierta = True

        cv2.putText(frame, f"Conteo Repeticiones: {conteo_repeticiones}", (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        cv2.imshow("Contando Repeticiones", frame)
        t = cv2.waitKey(1)  # Espera la pulsación de tecla por 1 milisegundo

        if t == 27:
            break
    raiz.destroy()
def umbral1():
    while True:
        global mano_abierta,conteo_repeticiones
        ret, frame = cap.read()

        frame = detector.encontrarmanos(frame)

        # Verificar el estado actual de la mano
        manos_info, cuadro = detector.encontrarposicion(frame, dibujar=False)
        if len(manos_info) != 0:
            dedos = detector.dedosarriba()
            #print(dedos)
            # Verificar el cambio de estado de la mano
            if dedos == [0, 0, 0, 0, 0] and mano_abierta:
                # La mano estaba abierta y ahora está cerrada
                mano_abierta = False
                conteo_repeticiones += 1
                print("Mano cerrada. Conteo de repeticiones:", conteo_repeticiones)
            elif dedos == [1, 1, 1, 1, 1] and not mano_abierta:
                # La mano estaba cerrada y ahora está abierta
                mano_abierta = True

        cv2.putText(frame, f"Conteo Repeticiones: {conteo_repeticiones}", (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        cv2.imshow("Contando Repeticiones", frame)
        t = cv2.waitKey(1) # Espera la pulsación de tecla por 1 milisegundo

        if t == 27:
            break
    raiz.destroy()
    
#interfaz
raiz=Tk()
raiz.title("App Fisioterapia")
miframe=Frame(raiz,width=480,height=400)
miframe.pack()

label1=Label(raiz,text="NIVEL 1" ,font=("Comic Sans Ms",18))
label1.place(x=100,y=50)
#se crea un boton el cual se ejecuta cuando es creado es por que se usa la funcion lambda para que se ejecute cuando se presioando el boton y no cuando se creado
boton1=Button(raiz,text="Presionar",font=("Comic Sans Ms",12),bg="darkorange",command=lambda: umbral())
boton1.place(x=110,y=100)
# Cargar y redimensionar la primera imagen
imagen1 = Image.open('../pngtree-five-fingers-claws-gestures-image_1465952.png')
imagen1 = imagen1.resize((100, 100), Image.ANTIALIAS)  # Ajusta el tamaño según tus necesidades
imagen1 = ImageTk.PhotoImage(imagen1)
im = Label(raiz, image=imagen1)
im.place(x=100, y=150)

# Cargar y redimensionar la segunda imagen
imagen2 = Image.open('../57980140-la-mano-con-el-icono-del-puño-cerrado-en-el-estilo-de-dibujos-animados-sobre-un-fondo-blanco.png')
imagen2 = imagen2.resize((100, 100), Image.ANTIALIAS)  # Ajusta el tamaño según tus necesidades
imagen2 = ImageTk.PhotoImage(imagen2)
im2 = Label(raiz, image=imagen2)
im2.place(x=100, y=250)

label2=Label(raiz,text="NIVEL 2",font=("Comic Sans Ms",18))
label2.place(x=300,y=50)
boton2=Button(raiz,text="Presionar",font=("Comic Sans Ms",12),bg="darkorange",command=lambda: umbral1())
boton2.place(x=310,y=100)

imagen3 = Image.open('../hand-human-open-free-vector.png')
imagen3 = imagen3.resize((100, 100), Image.ANTIALIAS)  # Ajusta el tamaño según tus necesidades
imagen3 = ImageTk.PhotoImage(imagen3)
im = Label(raiz, image=imagen3)
im.place(x=310, y=150)

# Cargar y redimensionar la segunda imagen
imagen4 = Image.open('../57980140-la-mano-con-el-icono-del-puño-cerrado-en-el-estilo-de-dibujos-animados-sobre-un-fondo-blanco.png')
imagen4 = imagen4.resize((100, 100), Image.ANTIALIAS)  # Ajusta el tamaño según tus necesidades
imagen4 = ImageTk.PhotoImage(imagen4)
im2 = Label(raiz, image=imagen4)
im2.place(x=310, y=250)

"""label3=Label(raiz,text="NIVEL 3",font=("Comic Sans Ms",18))
label3.place(x=100,y=200)
boton3=Button(raiz,text="Presionar",font=("Comic Sans Ms",12),bg="darkorange",command=lambda: codigo(3))
boton3.place(x=110,y=250)

label4=Label(raiz,text="NIVEL 4",font=("Comic Sans Ms",18))
label4.place(x=300,y=200)
boton4=Button(raiz,text="Presionar",font=("Comic Sans Ms",12),bg="darkorange",command=lambda: codigo(4))
boton4.place(x=310,y=250)
"""
raiz.mainloop()
# Variables para rastrear el estado actual de la mano y el conteo de repeticiones

cap.release()
cv2.destroyAllWindows()


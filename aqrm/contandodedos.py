import cv2 #Es la biblioteca OpenCV, utilizada para el procesamiento de imágenes y vídeo 
import seguimientomanos as sm  # Importa el módulo seguimientomanos que contiene la implementación del seguimiento de manos y se dan  alias sm para simplificar su uso en el código.

# Crea un objeto de la clase detectormanos con un umbral de confianza de detección del 75%
detector = sm.detectormanos(Confdeteccion=int(0.75))

# Inicia la captura de video desde la cámara (puede ajustar el argumento de VideoCapture según la cámara que estés utilizando)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Lee un frame de la cámara

    frame = detector.encontrarmanos(frame)  # Detecta y dibuja las manos en el frame

    # Dibuja un rectángulo negro en el frame
    cv2.rectangle(frame, (420, 225), (570, 425), (0, 0, 0), cv2.FILLED)
    
    # Muestra el texto "dedos" en el rectángulo negro
    cv2.putText(frame, "dedos", (425, 420), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 5)

    manosinfo, cuadro = detector.encontrarposicion(frame, dibujar=False)  # Obtiene la posición de las manos
    #print(manosinfo)

    if len(manosinfo) != 0: #se activa si al menos una mano está siendo detectada.
        dedos = detector.dedosarriba()  # Obtiene la información sobre qué dedos están levantados
        print(dedos)
        contar = dedos.count(1)  # Cuenta cuántos dedos están levantados es decir cuenta cuántos elementos con el valor 1

        # Dibuja el número de dedos levantados en el frame
        cv2.putText(frame, str(contar), (445, 375), cv2.FONT_HERSHEY_PLAIN, 10, (0, 255, 0), 25)

    cv2.imshow("contando dedos", frame)  # Muestra el frame con la información de dedos levantados es decir Utiliza la función 
                                        #cv2.imshow para mostrar el frame procesado en una ventana con el título "contando dedos"
    #se utiliza para pausar la ejecución del programa y esperar la entrada del usuario. En este caso, la espera es de 1 milisegundo
    t = cv2.waitKey(1)  # Espera la pulsación de tecla por 1 milisegundo
    if t == 27:  # Si la tecla 'Esc' (código 27 ascii) es presionada, sale del bucle
        break

cap.release()  # Libera la captura de video
cv2.destroyAllWindows()  # Cierra todas las ventanas abiertas por OpenCV

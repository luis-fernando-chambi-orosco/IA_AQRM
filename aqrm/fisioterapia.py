import cv2
import seguimientomanos as sm

detector = sm.detectormanos(Confdeteccion=int(0.75))

cap = cv2.VideoCapture(0)

# Variables para rastrear el estado actual de la mano y el conteo de repeticiones
mano_abierta = True  # Suponemos que la mano está abierta al inicio
conteo_repeticiones = 0

while True:
    ret, frame = cap.read()

    frame = detector.encontrarmanos(frame)

    # Verificar el estado actual de la mano
    manos_info, cuadro = detector.encontrarposicion(frame, dibujar=False)
    if len(manos_info) != 0:
        dedos = detector.dedosarriba()

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
    t = cv2.waitKey(1)

    if t == 27:
        break

cap.release()
cv2.destroyAllWindows()

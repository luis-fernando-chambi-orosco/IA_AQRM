import math #libreria para usar 
import cv2
import mediapipe as mp #libreria primaria para la deteccion de manos
import time

#creacion de la clase detector
class detectormanos():
    #se inicia los parametros de la deteccion 
    def __init__(self, mode=False, maxmanos=2, Confdeteccion=0.5, Confsegui=0.5):
        self.mode = mode    #creacion del objeto con su propia variable
        self.maxmanos = maxmanos    #lo mismo haremos con los objetos
        self.Confdeteccion = Confdeteccion
        self.Confsegui = Confsegui

        #creacion de los objetos que detectaran las manos y las dibujaran 
        self.mpmanos = mp.solutions.hands #usan mediapipe para las declaraciones
        self.manos = self.mpmanos.Hands(self.mode, self.maxmanos, self.Confdeteccion, self.Confsegui)
        self.dibujo = mp.solutions.drawing_utils
        self.tip = [4, 8, 12, 16, 20]  #declaracion de los dedos clave para la parte de arriba.

    #funcion para encontrar manos
    def encontrarmanos(self, frame, dibujar=True): #se hace le entregra de un frame
        imgcolor = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)   #proceso de correccion de color
        self.resultados = self.manos.process(imgcolor)  #procesa las imagenes para encontrar las imagenes 
        
        #definicion de los segmentos que trazan los nodos y longitudes de las manos
        if self.resultados.multi_hand_landmarks:
            for mano in self.resultados.multi_hand_landmarks:
                if dibujar:
                    self.dibujo.draw_landmarks(frame, mano, self.mpmanos.HAND_CONNECTIONS)
        return frame
    
    #funcion para encontrar las posicion de la mano
    def encontrarposicion(self, frame, manonum=0, dibujar=True):
        xlista = []
        ylista = []
        bbox = []   #entregra de coordenadas sobre puntos importantes de cada mano
        self.lista = [] #asi como el marco el cual rodea la mano
        if self.resultados.multi_hand_landmarks:
            mimano = self.resultados.multi_hand_landmarks[manonum]
            for id, lm in enumerate(mimano.landmark):
                alto, ancho, c = frame.shape #se extraen las dimensiones
                cx, cy = int(lm.x * ancho), int(lm.y * alto)
                xlista.append(cx)
                ylista.append(cy)
                self.lista.append([id, cx, cy])
                if dibujar:
                    cv2.circle(frame, (cx, cy), 5, (0, 0, 0), cv2.FILLED) #se dibujan los circulos
            xmin, xmax = min(xlista), max(xlista)
            ymin, ymax = min(ylista), max(ylista)
            bbox = xmin, ymin, xmax, ymax
            if dibujar:
                cv2.rectangle(frame, (xmin - 20, ymin - 20), (xmax + 20, ymax + 20), (0, 255, 0), 2)
        return self.lista, bbox

    #funcion para encontrar los dedos arriba 
    def dedosarriba(self):
        dedos = []
        if self.lista[self.tip[0]] [1] > self.lista[self.tip[0] - 1][1]: #utiliza la lista de arriba para 
            dedos.append(1)                     #establecer que esos deben tener la posicion mayor, para ser
        else:                                   #considerado dedo arriba.
            dedos.append(0)

        for id in range(1, 5):
            if self.lista[self.tip[id]][2] < self.lista[self.tip[id] - 2][2]:
                dedos.append(1)
            else:
                dedos.append(0)
        return dedos

    #detecta la distancia entre dedos.
    def distancia(self, p1, p2, frame, dibujar=True, r=15, t=3):
        x1, y1 = self.lista[p1][1:]
        x2, y2 = self.lista[p2][1:]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        if dibujar:
            cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), t)
            cv2.circle(frame, (x1, y1), r, (0, 0, 255), cv2.FILLED)
            cv2.circle(frame, (x2, y2), r, (0, 0, 255), cv2.FILLED)
            cv2.circle(frame, (cx, cy), r, (0, 0, 255), cv2.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)
        return length, frame, [x1, y1, x2, y2, cx, cy]

# -------------------------------------------------------------------
def main():
    ptiempo = 0
    ctiempo = 0

    cap = cv2.VideoCapture(0)

    detector = detectormanos()

    while True:
        ret, frame = cap.read()

        frame = detector.encontrarmanos(frame)
        lista, bbox = detector.encontrarposicion(frame)

        ctiempo = time.time()
        fps = 1 / (ctiempo - ptiempo)
        ptiempo = ctiempo
        cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        cv2.imshow("manos", frame)
        k = cv2.waitKey(1)

        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

        
         
                
                
                
		
import cv2
import seguimientomanos as sm

detector=sm.detectormanos(Confdeteccion=int(0.75))

cap=cv2.VideoCapture(0)

while True:
        
        ret,frame=cap.read()
        
        frame=detector.encontrarmanos(frame)
        
        cv2.rectangle(frame,(420,225),(570,425),(0,0,0),cv2.FILLED)
        
        cv2.putText(frame,"dedos",(425,420),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),5)
        
        manosinfo,cuadro=detector.encontrarposicion(frame,dibujar=False)
        #print(manosinfo)
        if len(manosinfo)!=0:
                dedos=detector.dedosarriba()
                print(dedos)
                contar=dedos.count(1)
                if contar==0:
                        cv2.putText(frame,str(contar),(445,375),cv2.FONT_HERSHEY_PLAIN,10,(0,255,0),25)
                elif contar==1:
                        cv2.putText(frame,str(contar),(445,375),cv2.FONT_HERSHEY_PLAIN,10,(0,255,0),25)
                elif contar==2:
                        cv2.putText(frame,str(contar),(445,375),cv2.FONT_HERSHEY_PLAIN,10,(0,255,0),25)
                elif contar==3:
                        cv2.putText(frame,str(contar),(445,375),cv2.FONT_HERSHEY_PLAIN,10,(0,255,0),25)
                elif contar==4:
                        cv2.putText(frame,str(contar),(445,375),cv2.FONT_HERSHEY_PLAIN,10,(0,255,0),25)
                elif contar==5:
                        cv2.putText(frame,str(contar),(445,375),cv2.FONT_HERSHEY_PLAIN,10,(0,255,0),25)
                        
        cv2.imshow("contando dedos",frame)
        t=cv2.waitKey(1) 
        if t==27 :
                break

cap.release()
cv2.destroyAllWindows()
        
        
        
        
        
#pip install imutils
import cv2
import imutils
import math


#download the cascades xml to the same file as the program 
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
   
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        facearea=gray[y:y +h*2//3, x:x+w]
        faceareacol = img[y:y*2//3 +h, x:x+w]
        eyes = eye_cascade.detectMultiScale(facearea)
        for (a,b,c,d) in eyes :
            
            cv2.circle(faceareacol, (a + 30,b + 30), 25 , (0, 0, 0), -1)
            
            if  a < (w)//2:
                cv2.line(faceareacol, (a +30 , b+ 30), (a + 100, b + 30), (0, 0, 0), 10)
            
            
        cv2.putText(img, "Ug Lee", (x, y + h + h//5 ), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 250, 150), 2) 
        cv2.imshow('Detecting Ugly Faces',img)
           
    
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()    

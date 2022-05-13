import cv2

import numpy as np

camera = cv2.VideoCapture(0)

def nothing(x):
    pass

#Renk bulmak için trackbar
cv2.namedWindow("frame")
cv2.createTrackbar("H1","frame",0,359,nothing)
cv2.createTrackbar("H2","frame",0,359,nothing)
cv2.createTrackbar("S1","frame",0,255,nothing)
cv2.createTrackbar("S2","frame",0,255,nothing)
cv2.createTrackbar("V1","frame",0,255,nothing)
cv2.createTrackbar("V2","frame",0,255,nothing)



while camera.isOpened():
    
    _,frame=camera.read()
    
    
    #Mavi rengi göster
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #Trackbar değerlerini al
    H1=int(cv2.getTrackbarPos("H1","frame")/2) #0-180 arasıdeğer alır
    H2=int(cv2.getTrackbarPos("H1","frame")/2)
    S1=cv2.getTrackbarPos("S1","frame")
    S2=cv2.getTrackbarPos("S2","frame")
    V1=cv2.getTrackbarPos("V1","frame")
    V2=cv2.getTrackbarPos("V2","frame")
    
    #Bulacağamız renk
    lower=np.array([H1,S1,V1])
    upper=np.array([H2,S2,V2])
    
    mask=cv2.inRange(hsv,lower,upper)
    
    res=cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow("Frame",frame)
    cv2.imshow("hsv",hsv)
    cv2.imshow("res",res)
    cv2.imshow("mask",mask)


    if cv2.waitKey(5)==ord("q"):
        break

camera.release()
cv2.destroyAllWindows()




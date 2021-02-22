import numpy as np
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
while(1):

    _,frame = cap.read()
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    out.write(frame)

    lower_mask = np.array([50,0,0])
    upper_mask = np.array([255,255,255])

    mask = cv2.inRange(hsv, lower_mask,upper_mask)
    res = cv2.bitwise_and(frame,frame,mask = mask)


    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray_image)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()

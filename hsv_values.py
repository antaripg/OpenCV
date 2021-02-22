import cv2
import numpy as np

gray = np.uint8([[[128,128,128 ]]])
hsv_gray = cv2.cvtColor(gray,cv2.COLOR_BGR2HSV)
print (hsv_gray)

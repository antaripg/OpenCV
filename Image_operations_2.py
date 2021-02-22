import numpy as np
import cv2

img = cv2.imread('test_image.jpg', cv2.IMREAD_COLOR)

#Resizing the Image
#cv2.resize(src, dsize[], dst[], fx[], fy[], interpolation]]]])
half_img = cv2.resize(img, (0, 0), fx = 0.15, fy = 0.15)

#IMAGE SIZES
print(img.shape)
print(half_img.shape)

sized_img = cv2.resize(img, (512, 512))
print(sized_img.shape)

#half_img[300,450] = [255,255,255]

#px = img[100,100]

#print(px)

#Region of IMAGE - img[start-x:end-x, start-y:end-y]
#half_img[300:450,450:600] = [255,255,255]

#******************************
#COPY AND PASTE --> The copy array and paste array should be of the same size
copy_part = half_img[200:450,350:600]
half_img[50:300,100:350] = copy_part
half_img[50:300,600:850] = copy_part



#cv2.imshow('image', img)
cv2.imshow('half_image', half_img)
#cv2.imshow('sized_img', sized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

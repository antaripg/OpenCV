import numpy as np
import cv2

#Reading the image
img = cv2.imread('test_image.JPG', cv2.IMREAD_COLOR)

#Drawing a line on the image cv2.line(image,starting,ending, color, linewidth)
cv2.line(img, (0,0), (150,150), (255,255,255), 15)


#Drawing a rectngle on the image cv2.line(image,top line, bottomline, color, linewidth)
cv2.rectangle(img, (15,25), (200,150), (0,255,0),15 )

#Drawing a circle cv2.circle(image, centre co-ordinate, radius, color, linewidth or fill)
cv2.circle(img, (100,63), 55, (0,0,255), -1 )

#Drawing a polygon with points as array
pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)

#Reshaping the array points into 1X2 array - as per the documentation opencv
pts = pts.reshape((-1,1,2))

# Using the polylines function cv2.polylines( image, [array of points], color, linewidth)
cv2.polylines(img, [pts], True, (0,255,255),3)

#Writing on the image
font = cv2.FONT_HERSHEY_SIMPLEX #defining the font
#writing the text on image with cv2.putText( image, 'TEXT', co-ordinates, font, size, color, word_thickness, Attempted anti-aliasing)
cv2.putText(img, 'OpenCV Tuts',(512,512),font, 1, (200,255,255), 2, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

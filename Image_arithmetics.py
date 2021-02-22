import numpy as np
import cv2


#Reading the images
logo= cv2.imread('python_logo.jpg',cv2.IMREAD_COLOR)
img1= cv2.imread('test_image_1.jpg',cv2.IMREAD_COLOR)
img2 = cv2.imread('test_image_2.jpg',cv2.IMREAD_COLOR)

sized_logo = cv2.resize(logo, (128, 128))
sized_img1 = cv2.resize(img1, (512, 512))
sized_img2 = cv2.resize(img2, (512, 512))

# Simple Numpy array addition
add = sized_img1 + sized_img2

# Using cv2.add(imag1,image2) adds pixel wise values of the pixels with a maximum value truncated to [255,255,255]
add1 = cv2.add(sized_img1,sized_img2)

#Weighted addition cv2.addWeighted(image1,weight of image 1, image2, weight of image2, gamma)
weighted = cv2.addWeighted(sized_img1,0.6,sized_img2,0.4,0)

#Performing Image on Image Arithmetics
rows,cols,channels = sized_logo.shape

roi = sized_img1[0:rows,0:cols]

#creating mask on the small image
#Converting the small image to grayscale
img2gray = cv2.cvtColor(sized_logo, cv2.COLOR_BGR2GRAY)

#Thresholding cv2.threshold(image_name, min.pixelvalue,max.pixelvalue, threshold type - binaryinverse)
# pixelvalue > 220 --> WHITE and then Inversed similarly for pixel_value< 220
ret,mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('sized_logo',sized_logo)
#Displaying the mask
cv2.imshow('mask',mask)

#referencing the blacked out area of the mask
#bitwise --> lowlevel logical operations

mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask_inv',mask_inv)


sized_img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
cv2.imshow('sized_img1_bg',sized_img1_bg)
sized_logo_fg  = cv2.bitwise_and(sized_logo,sized_logo, mask = mask)
cv2.imshow('sized_logo_fg',sized_logo_fg)

dst = cv2.add(sized_img1_bg,sized_logo_fg)
cv2.imshow('dst',dst)
sized_img1[0:rows,0:cols] = dst

cv2.imshow('res',sized_img1)

#Displaying the Images

# cv2.imshow('sized_img', sized_img)
# cv2.imshow('sized_img1', sized_img1)
# cv2.imshow('sized_img2', sized_img2)
# cv2.imshow('add', add)
# cv2.imshow('add1', add1)
# cv2.imshow('weighted', weighted)

cv2.waitKey(0)
cv2.destroyAllWindows()

# pylint: disable=no-member

import cv2

import numpy as np

img = cv2.imread('cameraman.png', 0)

kernel = np.ones((3, 3), np.uint8)

img2=cv2.erode(img,kernel,iterations=1)


#img3=cv2.dilate(img2,kernel,iterations=1)

#my observation is unless I perform dilation on the image the salt noise
# will not be removed completely, but it will just be reduced


cv2.imshow('Your amazing filtered Image', img2)

cv2.waitKey()
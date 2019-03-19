import cv2

import numpy as np

img = cv2.imread('cameraman.png', 0)

kernel = np.ones((3, 3), np.uint8)

img2=cv2.erode(img,kernel,iterations=1)


#img3=cv2.dilate(img2,kernel,iterations=1)


cv2.imshow('Your amazing filtered Image', img2)

cv2.waitKey()
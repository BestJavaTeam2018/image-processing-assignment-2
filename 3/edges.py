# pylint: disable=no-member

import cv2
import numpy as np

img = cv2.imread('lady.png', 0)
kernel=np.zeros((3,3), np.uint8)

dilation=cv2.dilate(img,kernel,iterations=1)-img

cv2.imshow('Your amazing filtered Image', dilation)


cv2.waitKey()

# Dilation can also be used for edge detection by taking the dilation of an image and then subtracting away the original image, thus highlighting just those new pixels at the edges of objects that were added by the dilation. For example, starting with
# pylint: disable=no-member

import cv2
import numpy as np

img = cv2.imread('Square-circle.png', 0)

kernelSq=cv2.getStructuringElement(cv2.MORPH_RECT,(11,11))

kernelcircle=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))


dilation1=cv2.dilate(img,kernelcircle,iterations=1)
cv2.imshow('using circle structure', dilation1)
cv2.imwrite( "square-circle-1.png", dilation1 );


dilation2=cv2.dilate(img,kernelSq,iterations=1)
cv2.imshow('using square structure', dilation2)
cv2.imwrite( "square-circle-2.png", dilation2 );




cv2.waitKey()

# pylint: disable=no-member

import cv2

import numpy as np

img = cv2.imread('cameraman.png', 1)

#kernel = np.ones((5, 5), np.uint8)

kernelSq=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))


img2=cv2.erode(img,kernelSq,iterations=1)


#my observation is unless I perform dilation on the image the salt noise
# will not be removed completely, but it will just be reduced


cv2.imshow('SaltCleared', img2)

cv2.imwrite( "cameraman erode.png", img2 );


cv2.waitKey()
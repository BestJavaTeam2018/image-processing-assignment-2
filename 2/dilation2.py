# pylint: disable=no-member

import cv2

img = cv2.imread('cameraman.png', 0)

kernelSq=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))


dilation=cv2.dilate(img,kernelSq,iterations=1)


cv2.imshow('Your amazing filtered Image', dilation)
cv2.imwrite( "cameraman-denoised.png", dilation );



cv2.waitKey()

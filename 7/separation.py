import cv2

img = cv2.imread('circle_and_lines.png', 0)

kernelDisk=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))

opening=cv2.morphologyEx(img, cv2.MORPH_OPEN, kernelDisk)

cv2.imshow('Your amazing filtered Image', opening)

cv2.waitKey()
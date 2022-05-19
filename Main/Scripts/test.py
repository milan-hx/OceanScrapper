import cv2
import numpy as np

img = cv2.imread("Main\Resources\lionfish.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

g_blur_img = cv2.GaussianBlur(gray_img, (7, 7), 0)

lapl_img = cv2.Laplacian(gray_img, cv2.CV_64F)

th, threshhold = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY)

print(th)

cv2.imshow('img', img)
cv2.imshow('gs_img', gray_img)
cv2.imshow('g_blur_img', g_blur_img)
cv2.imshow('laplacian', lapl_img)
cv2.imshow('threshhold', threshhold)



key=cv2.waitKey(0)

if(key == ord('q')):
    cv2.destroyAllWindows()


import cv2
import numpy as np

img = cv2.imread("resources/test3.png")

kernel = np.ones((5,5),np.uint8)

change_img_colour = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur_img = cv2.GaussianBlur(img,(7,7),0)
cannyimg = cv2.Canny(img, 100,100)
dialationimg = cv2.dilate(cannyimg,kernel,iterations=1)
erodedimg = cv2.erode(img,kernel,iterations=1)

cv2.imshow("changed image change_img_colour", blur_img)
cv2.imshow("changed image blur_img", img)
cv2.imshow("changed image canny", cannyimg)
cv2.imshow("changed image dialation", dialationimg)
cv2.imshow("changed image erode", erodedimg)

cv2.waitKey(0)

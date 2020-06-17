import cv2
import numpy as np
from function import stackImages
from function import getContours



shapes = cv2.imread("resources/shapes2.png")
gray_image = cv2.cvtColor(shapes, cv2.COLOR_BGR2GRAY)
blur_image = cv2.GaussianBlur(gray_image,(7,7),1)
image_canny = cv2.Canny(gray_image,50,50)
blank = np.zeros_like(gray_image)
shapes_copy = shapes.copy()
getContours(image_canny, shapes_copy)
group_image = stackImages(0.5,([shapes,gray_image,blur_image],[image_canny,shapes_copy,blank]))

# cv2.imshow("shapes orginal", shapes)
# cv2.imshow("gray image", gray_image)
cv2.imshow("group image", group_image)

cv2.waitKey(0)


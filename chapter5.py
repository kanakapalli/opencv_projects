import cv2
import numpy as np

image = cv2.imread("resources/Playing-cards.jpg")

width, height = 500,350

plts = np.float32([[132,85],[285,17],[181,190],[331,126]])
plts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(plts,plts2)
imageoutput = cv2.warpPerspective(image,matrix,(width,height))

cv2.imshow("image", image)
cv2.imshow("output image", imageoutput)
cv2.waitKey(0)

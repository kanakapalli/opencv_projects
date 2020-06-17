import cv2
import numpy as np

image = np.ones((512, 512, 3), np.uint8)

print(image.shape)

# change colour of img
image[:] = 0, 0, 255
# color a part
image[0:200, 250:320]= 0, 255, 0

# drawing a line
cv2.line(image,(0,0),(500,500),(255,0,0),5)
cv2.line(image,(10,0),(image.shape[1],image.shape[0]),(255,150,200),5)
# line (image , startingpoint , endingpoint, color, thinkness)

# drawing retangle
cv2.rectangle(image,(152,0),(400,420),(0,150,200),2)
cv2.rectangle(image,(0,0),(150,150),(0,250,0), cv2.FILLED)

# drawing cirecle
cv2.circle(image, (400,100),50,(255,255,0),5)
# circle (image, centerpoint, radius, color , thinkness)

# putting text on image
cv2.putText(image, "hola amigo",(300,100), cv2.FONT_HERSHEY_DUPLEX,1,(0,150,0),1 )
# putText( image, text, starting pooint, font, scale (size), color, thinkness)

cv2.imshow("black", image)
cv2.waitKey(0)
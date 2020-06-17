import cv2
import numpy as np
from function import stackImages

# colour detection
def onChange(a):
    pass

cv2.namedWindow("controles")
cv2.resizeWindow("controles", 640, 200)
cv2.createTrackbar("hue", "controles", 106, 179, onChange)
cv2.createTrackbar("hue_max", "controles", 179, 179, onChange)
cv2.createTrackbar("sat", "controles", 122, 255, onChange)
cv2.createTrackbar("sat_max", "controles", 225, 255, onChange)
cv2.createTrackbar("val", "controles", 0, 255, onChange)
cv2.createTrackbar("val_max", "controles", 225, 255, onChange)


while True:
    tesla = cv2.imread("resources/tesla.jpg")
    tesla_resized = cv2.resize(tesla,(300,200))
    hsv = cv2.cvtColor(tesla_resized, cv2.COLOR_BGR2HSV)

    hue = cv2.getTrackbarPos("hue","controles")
    hue_max = cv2.getTrackbarPos("hue_max","controles")
    sat = cv2.getTrackbarPos("sat","controles")
    sat_max = cv2.getTrackbarPos("sat_max","controles")
    val = cv2.getTrackbarPos("val","controles")
    val_max = cv2.getTrackbarPos("val_max","controles")
    print(hue,hue_max,sat,sat_max,val,val_max)
    lower = np.array([hue,sat,val])
    upper = np.array([hue_max,sat_max,val_max])

    mask = cv2.inRange(hsv,lower,upper)
    imageOutpu = cv2.bitwise_and(tesla_resized,tesla_resized,mask=mask)
    group = stackImages(0.5,([tesla_resized,hsv,mask,imageOutpu]))

    # cv2.imshow("tesla", tesla)
    # cv2.imshow("tesla_resized", tesla_resized)
    cv2.imshow("hsv", hsv)
    cv2.imshow("mask",mask)
    cv2.imshow("mask222",imageOutpu)
    cv2.imshow("grouoed", group)

    cv2.waitKey(1)
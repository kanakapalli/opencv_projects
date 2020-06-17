import cv2
import numpy as np


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def learing_contour(img,imgContour):

    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        # finsing area of each shape
        area = cv2.contourArea(cnt)
        print(area)
        # this conditions is to remove noise
        if area > 500:
            # drawing shapes on another images
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            # finding arc lenght
            peri = cv2.arcLength(cnt, True)
            print(peri)
            # finding edges of each shape
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True) # it will give the (x,y) of edges
            print(len(approx)) # no of edges
            objCor = len(approx)

            x, y, w, h = cv2.boundingRect(approx)

            if objCor == 3:
                objectType = "Tri"
            elif objCor == 4:
                aspRatio = w / float(h)
                if aspRatio > 0.98 and aspRatio < 1.03:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCor > 4:
                objectType = "Circles"
            else:
                objectType = "None"
            # drawing box arounf the shapre
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # putting text in side shape 
            cv2.putText(imgContour, objectType,
                        (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 0, 0), 2)


def getContours(img,drawOn):

    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        # finsing area of each shape
        area = cv2.contourArea(cnt)
        # this conditions is to remove noise
        x,y,w,h = 0,0,0,0
        if area > 500:
            # drawing shapes on another images
            # cv2.drawContours(drawOn, cnt, -1, (255, 0, 0), 3)
            # finding arc lenght
            peri = cv2.arcLength(cnt, True)
            # finding edges of each shape
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True) # it will give the (x,y) of edges
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            # drawing box arounf the shapre
            cv2.rectangle(drawOn, (x, y), (x + w, y + h), (0, 255, 0), 2)
    print(x,y,w,h)
    return w+x//2,y



def editor():
    def onChange(a):
        pass
    cv2.namedWindow("controles")
    cv2.resizeWindow("controles", 640, 200)
    cv2.createTrackbar("hue", "controles", 0, 179, onChange)
    cv2.createTrackbar("hue_max", "controles", 0, 179, onChange)
    cv2.createTrackbar("sat", "controles", 0, 255, onChange)
    cv2.createTrackbar("sat_max", "controles", 0, 255, onChange)
    cv2.createTrackbar("val", "controles", 0, 255, onChange)
    cv2.createTrackbar("val_max", "controles", 0, 255, onChange)

def mask(img):
    hue = cv2.getTrackbarPos("hue", "controles")
    hue_max = cv2.getTrackbarPos("hue_max", "controles")
    sat = cv2.getTrackbarPos("sat", "controles")
    sat_max = cv2.getTrackbarPos("sat_max", "controles")
    val = cv2.getTrackbarPos("val", "controles")
    val_max = cv2.getTrackbarPos("val_max", "controles")
    print(hue, hue_max, sat, sat_max, val, val_max)
    lower = np.array([hue, sat, val])
    upper = np.array([hue_max, sat_max, val_max])
    mask = cv2.inRange(img,lower,upper)
    cv2.imshow("mask", mask)

def getContours_of_doc(img , drawon):
    biggest = np.array([])
    maxArea = 0
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>5000:
            cv2.drawContours(drawon, cnt, -1, (255, 0, 0), 1)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            if area >maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    cv2.drawContours(drawon, biggest, -1, (255, 0, 0), 20)
    print(biggest)
    return biggest

def reorder_points(myPoints):
    myPoints = myPoints.reshape((4, 2))
    myPointsNew = np.zeros((4, 1, 2), np.int32)
    add = myPoints.sum(1)
    # print("add", add)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    # print("NewPoints",myPointsNew)
    return myPointsNew
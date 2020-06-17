import cv2
import numpy as np
from function import stackImages
from function import editor

framewidth = 640
frameheight = 480


cam = cv2.VideoCapture(0)
cam.set(3,framewidth)
cam.set(4,frameheight)

# editor()
#              skin = ,[90,29,24,120,255,255]     blue= [0,77,79,15,255,255],                      low light face detection ,[0,0,51,170,255,255]
mycolour =[[5, 107, 0, 19, 255, 255],
            [133, 56, 0, 159, 156, 255],
            [57, 76, 0, 100, 255, 255],
            [90, 48, 0, 118, 255, 255]]

dor_colour = [[51, 153, 255],  ## BGR
                 [255, 0, 255],
                 [0, 255, 0],
                 [255, 0, 0]]
my_points = []   #[x,y , corlorId]

def getContours(img,drawOn):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True) # it will give the (x,y) of edges
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            # cv2.rectangle(drawOn, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return w + x// 2, y

def findcolor(img,mycolour,dor_colour):
    hsv1 = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    count = 0
    newpoint=[]
    for color in mycolour:
        print("1")
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(hsv1, lower, upper)
        x,y = getContours(mask, final_result)
        print("2")
        cv2.circle(final_result,(x,y),10,dor_colour[count],cv2.FILLED)
        if x!= 0 and y != 0:
            newpoint.append([x,y,count])
        count += 1
        print("3")
    return newpoint

def draw_points(my_points,mycolour):
    for points in my_points:
        print(points)
        cv2.circle(final_result,(points[0],points[1]),10,mycolour[points[2]],cv2.FILLED)

while True:
    success, img = cam.read()
    final_result = img.copy()

    np = findcolor(img, mycolour, dor_colour)
    if len(np)!=0:
        for i in np:
            my_points.append(i)
        draw_points(np,dor_colour)
    cv2.imshow("res", final_result)
    cv2.waitKey(1)
    stackImages(0.5, [img,img])
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
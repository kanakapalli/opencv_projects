import cv2
import numpy as np
from function import stackImages
from function import getContours_of_doc
from function import reorder_points

widthImg=540
heightImg =640
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4,480)
cap.set(10,100)

def preProcessing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    kernel = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny,kernel,iterations=2)
    imgThres = cv2.erode(imgDial,kernel,iterations=1)
    group = stackImages(0.5,[[img,imgGray,imgBlur],[imgCanny,imgDial,imgThres]])
    cv2.imshow("preprocessing", group)
    return imgThres





def cutting_doc(image , biggest_approx):
    biggest_approx = reorder_points(biggest_approx)

    plts = np.float32(biggest_approx)
    plts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv2.getPerspectiveTransform(plts, plts2)
    imageoutput = cv2.warpPerspective(image, matrix, (widthImg, heightImg))
    imageoutput = imageoutput[20:imageoutput.shape[0] - 20, 20:imageoutput.shape[1] - 20]
    imageoutput = cv2.resize(imageoutput, (widthImg, heightImg))
    return imageoutput


while True:
    success, img = cap.read()
    final = img.copy()
    tkae = img.copy()

    preProcessed_image = preProcessing(img.copy())
    biggest = getContours_of_doc(preProcessed_image, drawon=final)
    if biggest.size != 0:
        output = cutting_doc(tkae, biggest)


    cv2.imshow("contures after preprocessing", final)
    cv2.imshow("final", output)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
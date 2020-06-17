import cv2


faceCascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

image = cv2.imread("resources/magiee.JPG")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(gray, 1.1, 4)

for(x,y,width, height) in faces:
    cv2.rectangle(image,(x,y),(x+width, y + height),(255,0,0),3)


cv2.imshow("image", image)
cv2.waitKey(0)


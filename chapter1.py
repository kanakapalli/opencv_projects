import cv2
#
# print("package imported")
#
# # ------------------------------------------------------------------------------
#
# # # importing image
img = cv2.imread("resources/test3.png")
cv2.imshow("outpput", img)
cv2.waitKey(1000)  # if it 0 it will stay till we close |||| if number it will stay for that many mill seconds
#
#
#
# # ------------------------------------------------------------------------------
#
# # importing video
cap = cv2.VideoCapture("resources/video.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("title", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# ------------------------------------------------------------------------------

#  importing web cam

# add 0 at videocapture will give default wen cam output if we have another came use 1 to swift

cap = cv2.VideoCapture(0)
# set means settings
cap.set(3, 640) # 3 is id for height
cap.set(4,480)  #4  is id for width
cap.set(10,1000) #10 is id for birghtness
while True:
    success, img = cap.read()
    cv2.imshow("title", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




# ------------------------------------------------------------------------------

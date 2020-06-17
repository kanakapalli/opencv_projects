import cv2

img = cv2.imread("resources/guitar.jpg")
# it will x and -y of the image with 3 = rgb
resized_image = cv2.resize(img, (300,200))
croped_image = img[0:200 , 200:500]
# for crop ------> height , width

print(img.shape)
cv2.imshow("orginal", img)
cv2.imshow("resized", resized_image)
cv2.imshow("cropped", croped_image)

cv2.waitKey(0)  # if it 0 it will stay till we close |||| if number it will stay for that many mill seconds

import cv2

img = cv2.imread("C:\\Users\\shah2\\Pictures\\Dell Mobile Connect\\20210822_154927.jpg")

cv2.imshow("TestScreen", img)  # Any window name can be written

cv2.waitKey(0)

# 0 => until any key is pressed ... otherwise takes delay in milliseconds
# if we will not use above command the image will be seen but very quickly disappear.

cv2.destroyAllWindows()

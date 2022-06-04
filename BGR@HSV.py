import cv2

img = cv2.imread('test.png')
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("Original Image Output Screen 1", img)
cv2.imshow("HSV image output screen 2", img_HSV)

cv2.waitKey(0)

cv2.destroyAllWindows()

import cv2

img = cv2.imread("C:\\Users\\shah2\\Pictures\\Dell Mobile Connect\\20210822_154927.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # colourful => gray
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)  # odd no.s only allowed in second parameter ... blurs the img
img_edges_canny = cv2.Canny(img, 100, 100)  # only edges of image ... if you want DECREASE edges INCREASE the threshold values

cv2.imshow("Output screen 1 of image", img)
cv2.imshow("Output screen 2 of gray image", img_gray)
cv2.imshow("Output screen 3 of blur image", img_blur)
cv2.imshow("Output screen 4 of canny image", img_edges_canny)

cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)

cv2.destroyAllWindows()

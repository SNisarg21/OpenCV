import cv2

# Hue has maximum of 360 values but in opencv we 180 (total) values for hue


def empty(value):
    pass


img = cv2.imread('test.png')
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Minimum", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Maximum", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Saturation Minimum", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Saturation Maximum", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Value Minimum", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Value Maximum", "TrackBars", 255, 255, empty)
while True:
    HueMinimum = cv2.getTrackbarPos('Hue Minimum', 'TrackBars')
    print(HueMinimum)

# cv2.imshow("Output screen 1 : Original Image", img)
# cv2.imshow("Output screen 2 : HSV Image", img_HSV)

cv2.waitKey(0)

cv2.destroyAllWindows()

import cv2

img = cv2.imread('test.png')

# shape print jar kela tar agodar fy yetay mag fx

# pan apan resize kartana agodar fx det asto mag fy

print(img.shape)

img_resized = cv2.resize(img, (500, 700))

print(img_resized.shape)

cv2.imshow("Resized_image output screen 1", img_resized)

cv2.waitKey(0)

# images are nothing but array of pixels.

# image crop kartana pan agodar fy mag fx.

image_Cropped = img[330:413, 45:189]

cv2.imshow("Cropped Image output screen 2", image_Cropped)

cv2.waitKey(0)

cv2.destroyAllWindows()

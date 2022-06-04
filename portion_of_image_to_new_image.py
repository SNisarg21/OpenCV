import cv2
import numpy

img = cv2.imread('test.png')

pts1 = numpy.float32([[1216, 112], [1364, 112], [1216, 189], [1364, 189]])
pts2 = numpy.float32([[308, 0], [308, 592], [0, 0], [0, 592]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
img_portion = cv2.warpPerspective(img, matrix, (308, 592))

# Cannot Resize the image in joining methods ... also both need to have same number of channels (i.e. one gray and one rgb not allowed) because they are matrices.

img_portion_joined_horizontally = numpy.hstack((img_portion, img_portion))
img_portion_joined_vertically = numpy.vstack((img_portion, img_portion))

cv2.imshow("Portion of image rotated clockwise by 90deg output screen 1", img_portion)
cv2.imshow("Portion of image rotated clockwise by 90deg and joined horizontally output screen 2", img_portion_joined_horizontally)
cv2.imshow("Portion of image rotated clockwise by 90deg and joined vertically output screen 3", img_portion_joined_vertically)

# Assignment creating mirror image in x and y direction

pts3 = numpy.float32([[0, 0], [592, 0], [0, 308], [592, 308]])
pts4 = numpy.float32([[592, 0], [0, 0], [592, 308], [0, 308]])
pts5 = numpy.float32([[0, 308], [592, 308], [0, 0], [592, 0]])
pts6 = numpy.float32([[592, 308], [0, 308], [592, 0], [0, 0]])

matrix1 = cv2.getPerspectiveTransform(pts1, pts3)
img_portion1 = cv2.warpPerspective(img, matrix1, (592, 308))

matrix2 = cv2.getPerspectiveTransform(pts1, pts4)
img_portion2 = cv2.warpPerspective(img, matrix2, (592, 308))

matrix3 = cv2.getPerspectiveTransform(pts1, pts5)
img_portion3 = cv2.warpPerspective(img, matrix3, (592, 308))

matrix4 = cv2.getPerspectiveTransform(pts1, pts6)
img_portion4 = cv2.warpPerspective(img, matrix4, (592, 308))

img_portion5 = numpy.hstack((img_portion1, img_portion2))
img_portion6 = numpy.hstack((img_portion3, img_portion4))
img_portion7 = numpy.vstack((img_portion5, img_portion6))

cv2.imshow("Output Screen For Assignment", img_portion7)

cv2.waitKey(0)

cv2.destroyAllWindows()


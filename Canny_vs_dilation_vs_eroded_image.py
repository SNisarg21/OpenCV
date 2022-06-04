import cv2
import numpy

# To resize the output screen => image_name = cv2.resize(image_name, (size_in_x, size_in_y))
# To make canny image edges thicker => Dilation
# To make canny image edges thinner => Eroded
# To do this we to define matrix hence also imported Numpy


matrix_kernel = numpy.ones((5, 5))  # ones => all values to be 1 ... you can also add type of object by adding 'matrix_kernel = numpy.ones((5, 5),uint8)' (=> unsigned bit upto 8 bits i.e. from 0 to 255)


img = cv2.imread("C:\\Users\\shah2\\Pictures\\Dell Mobile Connect\\20210822_154927.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # colourful => gray

img_edges_canny = cv2.Canny(img, 100, 100)  # only edges of image ... if you want DECREASE edges INCREASE the threshold values
img_edges_canny = cv2.resize(img_edges_canny, (300, 300))

img_edges_dilation = cv2.dilate(img_edges_canny, matrix_kernel, iterations=1)  # here iterations => thickness ... it is optional ... to INCREASE Thickness, INCREASE the iterations
img_edges_dilation = cv2.resize(img_edges_dilation, (300, 300))

img_edges_eroded_of_canny = cv2.dilate(img_edges_canny, matrix_kernel, iterations=1)  # here iterations => thinness ... it is optional ... to INCREASE Thinness, INCREASE the iterations
img_edges_eroded_of_canny = cv2.resize(img_edges_eroded_of_canny, (300, 300))

img_edges_eroded_of_dilation = cv2.dilate(img_edges_dilation, matrix_kernel, iterations=1)  # here iterations => thinness ... it is optional ... to INCREASE Thinness, INCREASE the iterations
img_edges_eroded_of_dilation = cv2.resize(img_edges_eroded_of_dilation, (300, 300))

cv2.imshow("Output screen 1 of canny image", img_edges_canny)
cv2.imshow("Output screen 2 of Dilation image", img_edges_dilation)
cv2.imshow("Output screen 3 of Eroded image of canny image", img_edges_eroded_of_canny)
cv2.imshow("Output screen 4 of Eroded image of dilation image", img_edges_eroded_of_dilation)


cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)


cv2.destroyAllWindows()


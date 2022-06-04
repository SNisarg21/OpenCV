import cv2
import numpy


img = numpy.zeros((512, 512, 3))  # 512 by 512 boxes => gray scale image
img[:] = (255, 0, 0)  # slicing for coloring entire image
print(img.shape)

img_with_line = cv2.line(img, (0, 0), (512, 512), color=(123, 214, 444), thickness=2)  # parameter1 => image_name , parameter2 = pt1 , parameter3 = pt2
img_with_rectangle = cv2.rectangle(img, (50, 50), (300, 200), color=(123, 214, 444), thickness=2)  # parameter1 => image_name , parameter2 = pt1 , parameter3 = pt2
img_with_circle = cv2.circle(img, (350, 350), 100, color=(123, 214, 444), thickness=2)  # parameter1 => image_name , parameter2 = center ,parameter3 = radius
img_with_text = cv2.putText(img, "Image is array of pixels", (50, 242), fontScale=1, fontFace=cv2.FONT_HERSHEY_COMPLEX, color=(123, 214, 444), thickness=2)  # parameter1 => image_name , parameter2 = starting position ,parameter3 = Fontscale (congested ka nahi), parameter4 = Font name
img_with_arrowed_line = cv2.arrowedLine(img, (0, 512), (170, 248), color=(123, 214, 444), thickness=2)  # parameter1 => image_name , parameter2 = pt1 ,parameter3 = pt2
img_with_ellipse = cv2.ellipse(img, (250, 242), (275, 200), 45, 0, 360, color=(123, 214, 444), thickness=2)  # parameter1 => image_name , parameter2 = center, parameter3 => axes length (major axis length, minor axis length)

# img_with_square sathi parameter2 and parameter3 of img_with_rectangle che x aani y co-ordinate same pahije

# original grayscale image automatically got modified to image with line, rectangle, circle, TEXT, Arrowed line, Ellipse

cv2.imshow("Test screen 1", img)

cv2.waitKey(0)

cv2.destroyAllWindows()

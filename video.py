import cv2

# Remember video is nothing but series of images

vid = cv2.VideoCapture(0) # 0=>webcam ... jar dusra konta asel tar video cha path specify kara baki sagla same

while True:
    success, img = vid.read()
    cv2.imshow("Video Webcam", img)
    if cv2.waitKey(1) == ord("q"): # Until q on keyboard is pressed
        break

cv2.destroyAllWindows()

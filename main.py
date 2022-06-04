# 1. Importing module cv2 => Computer Vision 2
#
# 2. Now cv2 is a object in which there are multiple methods which we are going to use.
#
# 3. loading and viewing the image.
#     a. loading => cv2.imread method : Takes parameter as Image Path <=> this is stored in a variable so that it can used while viewing
#     Note : While giving the path as parameter remember that Special meaning of escape sequence '\' should be avoided by either using (r'Path') or by using '\\' instead of '\'
#     b. viewing => cv2.imshow method : Takes parameter as Name of Output Window screen and variable name in which image is been loaded
#     Note : Window Screen name can be anything
#     c. Waiting time for output window screen using method cv2.waitkey : Takes parameter as time in milliseconds
#     Note :  0 => until any key is pressed ... otherwise takes delay in milliseconds and if we will not use above command the image will be seen but very quickly disappear.
#     d. destroying wimdows once task is completed => cv2.destroyAllWindows()
#
# 4. loading and viewing the video.
#     Note : Remember video is nothing but series of images
#     a. loading => cv2.VideoCapture method : Takes parameter as Video Path <=> this is stored in a variable so that it can used while viewing
#     Note : i. 0 is the parameter for webcam ... jar dusra konta asel tar video cha path specify kara baki sagla same
#            ii. While giving the path as parameter remember that Special meaning of escape sequence '\' should be avoided by either using (r'Path') or by using '\\' instead of '\'
#     b. while True:
#         success, img = vid.read()
#         cv2.imshow("Video Webcam", img)
#         if cv2.waitKey(1) == ord("q"): # Until q on keyboard is pressed
#             break
#     c.  destroying wimdows once task is completed => cv2.destroyAllWindows()
#
# 5. Resizing and cropping the image
#     a. Resizing :
#         i. Knowing the size of the image => variable_name_used_to_load_the_image.shape
#         ii. cv2.resize => Takes two parameters variable_name_used_to_load_the_image and new size as a tuple <=> and store this in new variable and hence while viewing this resized image use this new variable
#         Note : While giving the size as tuple make sure you give in format '(fx, fy)'
#     b. Cropping :
#         i. variable_name_used_to_load_the_image[fy1:fy2, fx1:fx2] <=> and store this in new variable and hence while viewing this cropped image use this new variable
#         Note : while using Slicing remember that first fy comes then fx
#
# 6. Getting Portion of an image using numpy module
#     Import numpy module
#     pts_in_original_image = numpy.float32([[1216, 112], [1364, 112], [1216, 189], [1364, 189]])
#     pts_in_ideal_form_as_we_want = numpy.float32([[308, 0], [308, 592], [0, 0], [0, 592]])
#     matrix = cv2.getPerspectiveTransform(pts_in_original_image, pts_in_ideal_form_as_we_want)
#     img_portion = cv2.warpPerspective(img, matrix, (308, 592))
#     viewing this img_portion
#     Note : Cannot Resize the image in joining methods ... also both need to have same number of channels (i.e. one gray and one rgb not allowed) because they are matrices.
#
# 7. Stacking the images horizontally and vertically
#    img_portion_joined_horizontally = numpy.hstack((img_portion, img_portion))
#    img_portion_joined_vertically = numpy.vstack((img_portion, img_portion))
#
# 8. Creation of images ... starting with basic shapes
#


import cv2
import os
# img = cv2.imread("DevOps-LifeCycle.jpg", 1)

import glob

img = cv2.imread("galaxy.jpg", 0)

print(img.shape)
print(img.ndim)

# Can be used as int(img.shape[1]//2), int(img.shape[0]//2) as well
resized_image = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("galaxy_reisized.jpg", resized_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()


# def batchImgResize(filename):
#     img_name = cv2.imread('images/'+filename, 1)
#     new_image = cv2.resize(img_name, (100, 100))
#     return new_image
#
#
# files = os.listdir('images')
# for file in files:
#     if file.endswith('.jpg'):
#         cv2.imwrite('New' + file, batchImgResize(file))


"""
Code to Image resizing files in Batch

"""

images = glob.glob("images/*.jpg")
for image in images:
    img = cv2.imread(image, 0)
    re = cv2.resize(img, (100, 100))
    cv2.imshow("Resized file", re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image, re)

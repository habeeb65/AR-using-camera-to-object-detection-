import cv2 as cv
from cv2 import aruco

marker_dict =  cv.aruco.getPredefinedDictionary(cv.aruco.DICT_4X4_250)

MARKER_SIZE = 400  # pixels

for id in range(10):

    marker_image = aruco.generateImageMarker(marker_dict, id, MARKER_SIZE)
    # cv.imshow("img", marker_image)
    cv.imwrite(f"markers/markder_{id}.png", marker_image)
    # cv.waitKey(0)
    # break

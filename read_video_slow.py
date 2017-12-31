from imutils.video import FPS
import numpy as np
import argparse
import imutils
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-v","--video",required=True,help="path to the input videl file")
args = vars(ap.parse_args())


stream = cv2.VideoCapture(args["video"])
fps = FPS().start()



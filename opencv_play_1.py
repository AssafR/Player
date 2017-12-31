import numpy as np
import cv2

#video = "../videos/sample.avi"
video = r'C:\Users\ASSAF\Downloads\The.Orville.S01E01.HDTV.x264-SVA[ettv]\The.Orville.S01E01.HDTV.x264-SVA[ettv].mkv'
video_capture = cv2.VideoCapture(video)
video_length = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

count = 0
while(True):
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        if not ret:
            break

        count += 1

print video_length, count
# When everything done, release the capture
video_capture.release()
cv2.destroyAllWindows()
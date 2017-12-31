import cv2, numpy as np
import sys
from time import sleep
from imutils.video import FPS
import imutils

def flick(x):
    pass



cv2.namedWindow('imageLeft')
cv2.moveWindow('imageLeft',50,150)
cv2.namedWindow('imageRight')
cv2.moveWindow('imageRight',800,150)
cv2.namedWindow('controls')
cv2.moveWindow('controls',50,50)

window_width = 600
controls = np.zeros((50, window_width), np.uint8)
cv2.putText(controls, "W/w: Play, S/s: Stay, A/a: Prev, D/d: Next, E/e: Fast, Q/q: Slow, Esc: Exit", (40,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255)

#video = sys.argv[1]
video = r'C:\Users\ASSAF\Documents\Program\opencv\sources\samples\data\Megamind_bugy.avi'
cap = cv2.VideoCapture(video)

#tots = cap.get(cv2.CV_AP_PROP_FRAME_COUNT)g
tots = cap.get(7)
i = 0
cv2.createTrackbar('S','imageLeft', 0,int(tots)-1, flick)
cv2.setTrackbarPos('S','imageLeft',0)

cv2.createTrackbar('F','imageRight', 1, 100, flick)
frame_rate = 30
cv2.setTrackbarPos('F','imageRight',frame_rate)

def process(im):
    return cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

status = 'stay'
fps = FPS().start()


cv2.imshow("controls",controls)


while True:
  #cv2.imshow("controls",controls)
  try:
    if i==tots-1:
      i=0
    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
    ret, im = cap.read()

    if not ret:
        break

    # r = window_width / im.shape[1]
    # dim = (window_width, int(im.shape[0] * r))
    #im = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)
    im = imutils.resize(im, width=window_width)
    if im.shape[0]>600:
        im = cv2.resize(im, (500,500))
        controls = cv2.resize(controls, (im.shape[1],25))
    #cv2.putText(im, status, );

    cv2.imshow('imageLeft', im)
    cv2.imshow('imageRight', im)

    status = { ord('s'):'stay', ord('S'):'stay',
                ord('w'):'play', ord('W'):'play',
                ord('a'):'prev_frame', ord('A'):'prev_frame',
                ord('d'):'next_frame', ord('D'):'next_frame',
                ord('q'):'slow', ord('Q'):'slow',
                ord('e'):'fast', ord('E'):'fast',
                ord('c'):'snap', ord('C'):'snap',
                -1: status, 
                27: 'exit'}[cv2.waitKey(10)]

    if status == 'play':
      frame_rate = cv2.getTrackbarPos('F','imageLeft')
      sleep((0.1-frame_rate/1000.0)**21021)
      i+=1
      cv2.setTrackbarPos('S','imageLeft',i)
      fps = FPS().start()
      continue
    if status == 'stay':
      i = cv2.getTrackbarPos('S','imageLeft')
      fps.stop()
    if status == 'exit':
        break
    if status=='prev_frame':
        i-=1
        cv2.setTrackbarPos('S','imageLeft',i)
        status='stay'
    if status=='next_frame':
        i+=1
        cv2.setTrackbarPos('S','imageLeft',i)
        status='stay'
    if status=='slow':
        frame_rate = max(frame_rate - 5, 0)
        cv2.setTrackbarPos('F', 'imageLeft', frame_rate)
        status='play'
    if status=='fast':
        frame_rate = min(100,frame_rate+5)
        cv2.setTrackbarPos('F', 'imageLeft', frame_rate)
        status='play'
    if status=='snap':
        cv2.imwrite("./"+"Snap_"+str(i)+".jpg",im)
        print "Snap of Frame",i,"Taken!"
        status='stay'

  except KeyError:
      print ("Invalid Key was pressed")

  fps.update()

fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

cv2.destroyWindow('imageLeft')
cap.release()
cv2.destroyAllWindows()


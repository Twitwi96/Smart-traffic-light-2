from picamera.array import PiRGBArray
import picamera.array
import numpy as np
import time
import cv2
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

for i in (23, 25, 16, 21):
    GPIO.setup(i, GPIO.OUT)

# cam = PiCamera()
#cam.resolution=(480,480)
#cam.framerate=30
#raw=PiRGBArray(cam, size=(480,480))

cam=cv2.VideoCapture(0)
cam.set(4,480) #Width=480
cam.set(5,480) #Height=480
cam.set(6,30) #FrameRate = 30
raw=PiRGBArray(cam, size=(480,480))

time.sleep(0.1)

colorLower = np.array([0,100,100])
colorUpper = np.array([179,255,255])

initvert = 0
inithoriz = 0
counter = 0

for frame in cam.capture_continuous(raw, format="bgr", use_video_port=True):
    frame = frame.array
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(hsv,colorLower,colorUpper)
    mask = cv2.blur(mask,(3,3))
    mask= cv2.dilate(mask,None,iterations=5)
    mask= cv2.erode(mask,None,iterations=1)
    mask= cv2.dilate(mask,None,iterations=3)
    
    me,thresh = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)

    cnts = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    vert = 0
    horiz = 0 
    
    if len(cnts) > 0:
        for c in cnts:
            (x,y),radius = cv2.minEnclosingCircle(c)
            center = (int(x),int(y))
            radius = int(radius)
            cv2.circle(frame,center,radius,(0,255,0),2)

            x = int(x)
            y = int(y)
            
            if 180 < x < 300:
                if y > 300:
                    vert = vert +1
                elif y < 180:
                    vert = vert +1
                else:
                    vert = vert
            if 180 < y < 300:
                if x > 300:
                    horiz = horiz +1
                elif x < 180:
                    horiz = horiz +1
                else:
                    horiz = horiz
            if vert != initvert:
                print("Cars in vertical lane: ", str(vert))
                initvert = vert
                print("Cars in horizontal lane: ", str(horiz))
                inithoriz = horiz
                print ("----------------------------")

            if horiz != inithoriz:
                print("Cars in vertical lane: ", str(vert))
                initvert = vert
                print("Cars in horizontal lane: ", str(horiz))
                inithoriz = horiz
                print ("----------------------------")
            
        if vert < horiz:
            GPIO.output(23,GPIO.HIGH)
            GPIO.output(21,GPIO.HIGH)
            GPIO.output(16,GPIO.LOW)
            GPIO.output(25,GPIO.LOW)
        if horiz < vert:
            GPIO.output(16,GPIO.HIGH)
            GPIO.output(25,GPIO.HIGH)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(21,GPIO.LOW)

    
    cv2.imshow("Frame",frame)
    cv2.imshow("HSV",hsv)
    cv2.imshow("Thresh",thresh)
               
    raw.truncate(0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
GPIO.cleanup()

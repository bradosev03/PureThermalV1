#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from argparse import ArgumentParser
import threading
from time import gmtime, strftime

try:
    import cv2
except ImportError as e:
    print "[!] Import Error, please install python-opencv"
    sys.exit(1)

class CameraCapture(threading.Thread):
    def __init__(self,ID,verbose,display):
        threading.Thread.__init__(self)
        self.ID = ID
        self.windowName = "camera_{0}".format(ID)
        self.display = display
        self.verbose = verbose
    def run(self):
        print "Capturing from: {0}".format(self.windowName)
        if(self.display):
            capture_and_display(self.ID, self.windowName)
        else:
            capture(self.ID, self.windowName)

def findCameras():
    cameras = []
    for i in reversed(range(10)):
        sys.stdout.write("\r[~]Testing for a camera #{0}".format(i))
        sys.stdout.flush()
        try:
            cv2_cap = cv2.VideoCapture(i)
        except:
            continue
        if cv2_cap.isOpened():
            cameras.append(i)
    if len(cameras) == 0:
        print "[!] No Cameras connected to this device"
        sys.exit(1)
    return cameras

def capture_and_display(ID,windowName):
    cv2.namedWindow(windowName)
    cam = cv2.VideoCapture(ID)
    if cam.isOpened():
        rval, frame = cam.read()
    else:
        rval = False
    while rval:
        cv2.imshow(windowName, frame)
        rval, frame = cam.read()
        key = cv2.waitKey(20)
        if key == 27:
            sys.exit(0)
    cv2.destroyWindow(windowName)

def capture(ID,windowName):
    cam = cv2.VideoCapture(ID)
    while True:
        rval, frame = cam.read()
        filename = windowName + "_"+ strftime("%Y-%m-%d_%H:%M:%S", gmtime())+".jpeg"
        cv2.imwrite(filename, frame)
        key = cv2.waitKey(20)
        if key == 27:
            break;


def parse_options():
    parser = ArgumentParser(description="Capture Data From Multiple Cameras and store to your system")
    parser.add_argument("-v","--verbose",action="store_true", help="Enable Verbose Printing")
    parser.add_argument("-d","--display",action="store_true", help="If connected via HDMI cable, you can enable this feature")
    args = vars(parser.parse_args())
    return args

def main():
    args = parse_options()
    print args
    cameras = findCameras()
    threads = []
    for camera in cameras:
        threads.append(CameraCapture(camera,args["verbose"],args["display"]))
    for thread in threads:
        thread.start()


if __name__=="__main__":
    main()

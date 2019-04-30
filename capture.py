#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from argparse import ArgumentParser
import threading

try: 
    import cv2
except ImportError as e:
    print "[!] Import Error, please install python-opencv"
    sys.exit(1)

class SimpleThreader(threading.Thread):
    def __init__(self, ID):
        threading.Thread.__init__(self)
        self.ID = ID


def findCameras():
    cameras = []
    for i in reversed(range(10)):
        print "[~] Testing for a camera #{0} ".format(i)
        cv2_cap = cv2.VideoCapture(i)
        if cv2_cap.isOpened():
            cameras.append(i)
    if len(cameras) == 0:
        print "[!] No Cameras connected to this device"
        sys.exit(1)
    return cameras

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

if __name__=="__main__":
    main()

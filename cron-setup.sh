#! /bin/bash
sudo rmmod uvcvideo;
sudo modprobe uvcvideo nodrop=1 timeout=5000 quirks=0x80
/usr/bin/thermalpi > /dev/null 2>&1

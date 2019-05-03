# PureThermalV1
PureThermal capture for Raspberry Pi. Allows data collection from multiple cameras. 

# 

## Installation
Download the repository and run the following command
```bash
$ git clone https://github.com/bradosev03/PureThermalV1.git
$ cd PureThermalV1
$ bash make_deb.sh
$ cd ..
$ sudo apt install -f ./thermalpi_1.0.0.deb
```
To use the program simply run the following command:
```bash
$ thermalpi -h
usage: thermalpi [-h] [-v] [-d] [-t FILETYPE]

Capture Data From Multiple Cameras and store to your system
optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Enable Verbose Printing
  -d, --display         If connected via GUI, you can enable this feature
  -t FILETYPE, --filetype FILETYPE
                        File Extension Default: jpeg Choose Extension Type:
                        jpeg,jpg,jpe,bmp,png,ras,tiff
```
### Sample Usage:

```bash
$ thermalpi -t tiff -d 
```

To setup to start capturing images on boot use the following script:
```bash
$ crontab -e
$ @reboot /bin/bash /home/pi/PureThermalV1/cron-setup.sh
$ crontab -l 
```
This will create a startup script for when the raspberry pi reboots.

## Example Outputs:
[][./examples/example1.jpeg]
[][./examples/example2.jpeg]

## Known Issues:
  > C++ Wrapper STDERR: Warnings from the underlying C++ library will output to STDOUT. There is a known fix to this problem, however it involves recompiling the opencv library with proper STDOUT,STDERR hooks for python. 
  
 > Multithreading timeout on DEBIAN/Raspbian: Simple fix is running the following commands as superuser.`sudo rmmod uvcvideo` and `sudo modprobe uvcvideo nodrop=1 timeout=5000 quirks=0x80`.

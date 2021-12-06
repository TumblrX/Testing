#For Docker:
  -to build cotainer	    : sudo docker build -t appium_image .
  -to delete container	    : sudo docker rm my_appium
  -to run make file 	    : make -f filename
		 	    : make run
  -to create container 	    : sudo docker run -it --privileged -p 4723:4723 --name my_appium -v "$(pwd)"/appium_test:/appium_test  -v /dev/bus/usb:/dev/bus/usb appium_image
// -v to mountain a file
  -to open container bash   : sudo docker exec -it my_appium bash

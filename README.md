# Smart Traffic Lights 2
FLAMENT Dorian (Dorian.Flament@student.umons.ac.be)

NGUYEN Thuy hai (Thuy-Hai.Nguyen@student.umons.ac.be)

Faculty of Engineering, University of Mons (https://web.umons.ac.be/fr/), Belgium

Hardware/Software Platform course

Under the direction of Pr. Carlos VALDERRAMA (CarlosAlberto.VALDERRAMASAKUYAMA@umons.ac.be)

2017-2018

In folders above, you can find for each part (Tutorial Version, Improved Version 1 and Improved Version 2) :

- Pictures of our project
- Python codes used

and also : 
- README.txt file for general informations 
- PowerPoint presentation for a complete explanation of the project


# General Overview
The main goal of our project is to create traffic lights which allow to smartly manage the traffic on a road. 
To do so, traffic lights allow cars on the most blocked road to go through, by detecting the number of cars on each road with a webcam fixed above the intersection. Thanks to that, traffic jams and pollution caused by stopped cars are decreased.
Two further improvements are also performed : 

1) The automatic detection of road limits in order to adapt the system to all sizes of road of cross crossroads.
2) The possibility of giving the priority to emergency vehicles, like ambulances or fire engines, or globally to large vehicles (because it is long to fire up, involving traffics jams and pollution).


# Components of our project
This project is programmed in Python and the hardware used is the following :
- Raspberry Pi 3 (with OpenCV2 installed)
- USB Webcam
- Two traffic lights with LEDS (orange and green)
- Cables
- Resistors
- Structure and roads made by us

Schematic of the connections between components : 
![](http://liverpoolfc-fr.wifeo.com/images/c/cap/capture-d-e-cran-2018-05-23-a-17-52-30-im.jpg)

Global picture of the assembly performed : 
![](http://liverpoolfc-fr.wifeo.com/images/s/san/sans-titre.png)

# Project operation
To summarize the operation of the different codes used, here are some block diagrams and pictures. 

### Tutorial Version (detection of cars on the road) : 
"traffic.py" in folders above

- Global view of the code :

![alt tag](http://liverpoolfc-fr.wifeo.com/images/c/cap/capture-d-e-cran-2018-05-23-a-19-31-29.jpg)

- Some details for the part "Capture Frame Treatment", using the library opencv (CV2) :

Each treatment applied on the image captured by the webcam is showed and described as : 

![alt tag](http://liverpoolfc-fr.wifeo.com/images/3/330/33060423-1134416520032249-8026819840683540480-n.png)

1) Transform frame into array
2) Convert RGB to HSV
3) Threshold the HSV to exclude black and white (road and strips) 
4) Blur to ignore details (like windscreens or seats)
5) Dilate 10 times (in order to transform the car into a "block")
6) Erode
7) Dilate 5 times
8) Threshold

The conversion from RGB image to HSV is represented with this picture :

![alt tag](http://liverpoolfc-fr.wifeo.com/images/r/rgb/rgbhsv.png)

- After that, cars are framed with circles ("Find contours" part). The number of circles (and so of cars) are counted as described below.

![alt tag](http://liverpoolfc-fr.wifeo.com/images/s/san/sans-titre2.png)

- Focus on the "Counter and analysis" part (how to count the number of cars and how to react) : 

![alt tag](http://liverpoolfc-fr.wifeo.com/images/c/cap/capture-d-e-cran-2018-05-23-a-19-31-52.jpg)

- Some modifications are made to adapt the code of the Tutorial version for our building :
traffic_modif1.py in folders above

1) Increase dilatation for detection to be adapted to all kind of cars
2) View of all different masks (blur, dilate, erode) to see different steps of detection
3) Put all masks in one window for more visibility
4) Correct limits of the road to be adjusted to our structure
5) Make code work for any USB webcam


### Improved Version (automatic calibration of the road limits and priority to large vehicles) :

- Global Block Diagram of the improvements performed in this project : 

![alt tag](http://liverpoolfc-fr.wifeo.com/images/c/cap/capture-d-e-cran-2018-05-23-a-19-32-31.jpg)

#### Improvement 1 (automatic calibration)
traffic_modif2.py in folders above

- Picture showing calibration objects : 

![alt tag](http://liverpoolfc-fr.wifeo.com/images/c/cal/calibobj.png)

- The coordinates of the 4 calibration objects are detected. The image provided by the webcam is divided into 4 parts: each calibration object is associated with a zone. Thanks to that, we know where are the four corners of the crossroads, and so we know where are the roads. 

![alt tag](http://liverpoolfc-fr.wifeo.com/images/c/coo/coord.png)

- The calibration of the road limits is correctly made : vehicles in crossroads and outside road limits are not taken into account

![alt tag](http://liverpoolfc-fr.wifeo.com/images/i/imp/improv1.png)

#### Improvement 2 (priority vehicles)
traffic_modif3.py in folders above

- The circles to frame the cars are replaced by rectangles, in order to calculate the area of the vehicle more accurately :

![alt tag](http://liverpoolfc-fr.wifeo.com/images/c/cap/capture-d-e-cran-2018-05-23-a-18-26-48.jpg)

- When a large vehicle appears on a road (area > threshold) -> The other vehicles are not counted -> Green light for this road

![alt tag](http://liverpoolfc-fr.wifeo.com/images/i/imp/improv2.png)


# Click below to access to our Project Videos on Youtube : 
Tutorial Version :

[![video link youtube](http://liverpoolfc-fr.wifeo.com/images/c/cap/capture-d-e-cran-2018-05-21-a-16-12-18.jpg)]( https://www.youtube.com/watch?v=jQJlSoAfE3g&t=2s)


Improved Version 1 :

[![video link youtube](http://liverpoolfc-fr.wifeo.com/images/y/you/youtube-improved-version-1.jpg)]( https://www.youtube.com/watch?v=-3C68o-8WWs&feature=youtu.be)

Improved Version 2 : 

[![video link youtube](http://liverpoolfc-fr.wifeo.com/images/y/you/youtube-improved-version-2.jpg)]( https://www.youtube.com/watch?v=j2LM9ZPuFI4&feature=youtu.be)

"Untreated" Links for vidéos :

Tutorial Version : https://www.youtube.com/watch?v=jQJlSoAfE3g&t=2s

Improved Version 1 : https://www.youtube.com/watch?v=-3C68o-8WWs&feature=youtu.be

Improved Version 2 : https://www.youtube.com/watch?v=j2LM9ZPuFI4&feature=youtu.be

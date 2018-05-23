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
To do so, traffic lights let past cars on the most blocked road, by detecting the number of cars on each road with a webcam fixed above the intersection. Thanks to that, traffic jams and pollution caused by stopped cars are decreased.
Two further improvements are also performed : 

1) The automatic detection of road limits in order to adapt the system to all sizes of road of cross crossroads.
2) The possibility of giving the priority to emergency vehicles, like ambulances or fire engines, or globally to large vehicles (because it is long to fire up, involving traffics jams and pollution).

This project is programmed in Python and the hardware used is the following :
- Raspberry Pi 3
- USB Webcam
- Two traffic lights with LEDS (orange and green)
- Cables
- Structure and roads made by us

# Components of our project
This project is programmed in Python and the hardware used is the following :
- Raspberry Pi 3 (with OpenCV2 installed)
- USB Webcam
- Two traffic lights with LEDS (orange and green)
- Cables
- Structure and roads made by us

Schematic of the links between components : 
![alt tag](http://liverpoolfc-fr.wifeo.com/images/c/cap/capture-d-e-cran-2018-05-23-a-17-52-30.jpg)


Global picture of the building performed : 
![alt tag](http://liverpoolfc-fr.wifeo.com/images/s/san/sans-titre.png)

# Working of the codes
To summarize the working of different codes used, here is some block diagrams and pictures. 

## First, for the Tutorial Version (detection of cars on the road) :

- Global view of the code :
![alt tag](http://liverpoolfc-fr.wifeo.com/images/c/cap/capture-d-e-cran-2018-05-23-a-17-52-49.jpg)

- Then, some details for the part "Capture Frame Treatment", using the library opencv (CV2) : 
Each treatment applied on the image captured by the webcam is showed and described as : 
![alt tag](http://liverpoolfc-fr.wifeo.com/images/3/330/33060423-1134416520032249-8026819840683540480-n.png)

1.Transform frame into array
2.Convert RGB to HSV
3.Threshold the HSV to exclude black and white (road and strips) 
4. Blur to ignore details
5. Dilate 10 times (in order to transform the car in a "block")
6. Erode
7. Dilate 5 times
8. Threshold

- Finally, cars are framed with circles ("Find contours" part). These circles are counted as described below.
![alt tag](http://liverpoolfc-fr.wifeo.com/images/s/san/sans-titre2.png)

- Focus on the "Counter and analysis" part (how to count the number of cars and how to react ?) : 
![alt tag](http://liverpoolfc-fr.wifeo.com/images/c/cap/capture-d-e-cran-2018-05-23-a-17-53-00.jpg)

## Then, for the Improved Version (automatic calibration of the road limits and priority to large vehicles) :

- 


# Click below to access to our Project Videos on Youtube : 
Tutorial Version :

[![video link youtube](http://liverpoolfc-fr.wifeo.com/images/c/cap/capture-d-e-cran-2018-05-21-a-16-12-18.jpg)]( https://www.youtube.com/watch?v=jQJlSoAfE3g&t=2s)


Improved Version 1 :

[![video link youtube](http://liverpoolfc-fr.wifeo.com/images/y/you/youtube-improved-version-1.jpg)]( https://www.youtube.com/watch?v=-3C68o-8WWs&feature=youtu.be)

Improved Version 2 : 

[![video link youtube](http://liverpoolfc-fr.wifeo.com/images/y/you/youtube-improved-version-2.jpg)]( https://www.youtube.com/watch?v=j2LM9ZPuFI4&feature=youtu.be)


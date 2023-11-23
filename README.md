# Water Dispenser Spy on Raspberry Pi (version PoC)

### Description

This application is only the running part of the water dispenser spy project. Other parts of the project will be added to the documentation as they are completed.

Briefly, this is the Water Dispenser Spy that track and record your all dispensers data on the cloud. You will be able to access all your data from your mobile device. This project aims to be experimental, both for personal development and to make the home smarter. Finally, the project is completely open source and you can use it whatever you want.

This simple script will run on the Raspberry Pi and collect all the data from the water flow sensor and write it as a json array to a file on the disc.

Some not-so-necessary comfort zone Raspberry Pi Conf:

 - Python v3.9.0 or above
 - GIT v2.30.2 or above
 - VIM 8.0 or above

In the MVP of this part of the project, we use a Raspberry Pi and connect the water flow sensor with serial number YF-S201 to the appropriate pins in the socket of the Raspberry Pi.
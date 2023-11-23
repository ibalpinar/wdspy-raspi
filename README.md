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

By counting the pulses from the output of the sensor we can easily calculate water flow. Each pulse is approximately 2.25 milliliters and this also means approximately 450 pulses for 1 liter. Btw this isn't a precision sensor, and the pulse rate does vary a bit depending on the flow rate, fluid pressure and sensor orientation. It will need careful calibration if better than 10% precision is required. However, its great for basic measurement tasks! This is exactly enough for what we want to do. The pulse signal is a simple square wave so it is quite easy to log and convert into liters per minute using the following formula.

Pulse frequency (Hz) / 7.5 = flow rate in L/min.
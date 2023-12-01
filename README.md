# Water Dispenser Spy on Raspberry Pi (version PoC)

## Description

This application is only the running part of the water dispenser spy project. Other parts of the project will be added to the documentation as they are completed.

Briefly, this is the Water Dispenser Spy that track and record your all dispensers data on the cloud. You will be able to access all your data from your mobile device. This project aims to be experimental, both for personal development and to make the home smarter. Finally, the project is completely open source and you can use it whatever you want.

This simple script will run on the Raspberry Pi and collect all the data from the water flow sensor and write it as a json array to a file on the disc.

Some not-so-necessary comfort zone Raspberry Pi Conf:

 1. Python v3.9.0 or above
 2. GIT v2.30.2 or above
 3. VIM 8.0 or above

In the MVP of this part of the project, we use a Raspberry Pi and connect the water flow sensor with serial number YF-S201 to the appropriate pins in the socket of the Raspberry Pi.

By counting the pulses from the output of the sensor we can easily calculate water flow. Each pulse is approximately 2.25 milliliters and this also means approximately 450 pulses for 1 liter. Btw this isn't a precision sensor, and the pulse rate does vary a bit depending on the flow rate, fluid pressure and sensor orientation. It will need careful calibration if better than 10% precision is required. However, its great for basic measurement tasks! This is exactly enough for what we want to do. The pulse signal is a simple square wave so it is quite easy to log and convert into liters per minute using the following formula.

~~~
Pulse frequency (Hz) / 7.5 = flow rate in L/min.
~~~

## Installation
You can easily realize this project at home. The things you need to do are not very difficult. 

The requirements are as follows:

 1. Raspberry Pi
 2. Water Flow Sensor, model number YF-S201
 3. Water dispenser and Faucet (Sensor will be between these two stuff)
 4. Download all the repositories required by the project and complete the Installation steps (This part is still incomplete, it is being completed gradually)
 5. Lots of patience and passion

## Raspberry Pi Pinout table

Output from the PIs ```pinout``` command

```
   3V3  (1) o o (2)  5V
 GPIO2  (3) o o (4)  5V
 GPIO3  (5) o o (6)  GND
 GPIO4  (7) o o (8)  GPIO14
   GND  (9) o o (10) GPIO15
GPIO17 (11) o o (12) GPIO18
GPIO27 (13) o o (14) GND
GPIO22 (15) o o (16) GPIO23
   3V3 (17) o o (18) GPIO24
GPIO10 (19) o o (20) GND
 GPIO9 (21) o o (22) GPIO25
GPIO11 (23) o o (24) GPIO8
   GND (25) o o (26) GPIO7
 GPIO0 (27) o o (28) GPIO1
 GPIO5 (29) o o (30) GND
 GPIO6 (31) o o (32) GPIO12
GPIO13 (33) o o (34) GND
GPIO19 (35) o o (36) GPIO16
GPIO26 (37) o o (38) GPIO20
   GND (39) o o (40) GPIO21
```

## Raspberry Pi and YF-S201 Water Flow Sensor Connection

| Pin | Value  | Connected      | Connected     | Value  | Pin | 
|-----|--------|----------------|---------------|--------|-----|
| 1   | 3V3    | Sensor Power   | -             | 5V     | 2   |
| 3   | GPIO2  | -              | -             | 5V     | 4   |
| 5   | GPIO3  | -              | Sensor Ground | GND    | 6   |
| 7   | GPIO4  | -              | -             | GPIO14 | 8   |
| 9   | GND    | -              | -             | GPIO15 | 10  |
| 11  | GPIO17 | -              | -             | GPIO18 | 12  |
| 13  | GPIO27 | -              | -             | GND    | 14  |
| 15  | GPIO22 | -              | -             | GPIO23 | 16  |
| 17  | 3V3    | -              | -             | GPIO24 | 18  |
| 19  | GPIO10 | -              | -             | GND    | 20  |
| 21  | GPIO9  | -              | -             | GPIO25 | 22  |
| 23  | GPIO11 | -              | -             | GPIO8  | 24  |
| 25  | GND    | -              | -             | GPIO7  | 26  |
| 27  | GPIO0  | -              | -             | GPIO1  | 28  |
| 29  | GPIO5  | -              | -             | GND    | 30  |
| 31  | GPIO6  | -              | -             | GPIO12 | 32  |
| 33  | GPIO19 | Sensor Signal  | -             | GND    | 34  |
| 35  | GPIO19 | -              | -             | GPIO16 | 36  |
| 37  | GPIO26 | -              | -             | GPIO20 | 38  |
| 39  | GND    | -              | -             | GPIO21 | 40  |


## Important note:
This project is open source, so if you are currently reading this lines, and you believe you are competent, this is a great project to contribute to!

## A GIT Commit Message Be Like

 ```
 Add a new rule in README file [ISSUE-XX]
 ```
## License
Distributed under the GNU GPL. See [LICENSE](LICENSE) for more information.

Free Software, just for fun ;)
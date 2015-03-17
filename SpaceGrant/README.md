RobotEngine
===========

This project is to build robot systems in a logical way using Raspberry Pi and PiFace Digital.
It uses some FRP(functional reactive programming) techniques, but doesn't implement directly.
This project is written entirely in python and uses the Piface pfio library.

Engine: The heartbeat of the entire robot. This is called inside Robot2 to make the whole thing run.

LMotors: A class to represent the motors, and the values they require. Used only for testing.

Motors: Same thing as LMotor, but is the actual class used for driving the robot. Meaning it outputs stuff to the Pi pins.

Robot2: This is the main file. Meaning this is what you want to run when you're looking to test the program. It runs on boot of the pi.

Sensors: Super class for every sensor that is being used in the other files. 



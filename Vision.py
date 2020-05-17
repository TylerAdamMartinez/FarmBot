"""
Vision.py created by Tyler Adam Martinez: 
    Created: May 17, 2020
    Last Updated: May 17, 2020

Robot CV Design (Current plan as of May 17, 2020):
    @     Camera
    +     LiDar
    (A)   Camera Name

        Top
     _________
(A) | @     @ | (B)
    |    +    |
    |_________|

    
"""

import RPi.GPIO as GPIO
import time

class Vision: 
    """This Class defines all the CV functions for the robot"""
    def activate(self):
        """This code will turn on both cameras"""
        print("Camera A is ON")
        print("Camera B is ON")
        

    def shutdown(self):
        """This code will turn both cameras off"""
        print("Camera A is OFF")
        print("Camera B is OFF")
        

    def livefeed(self):
        """This code will display the current feed of the cameras"""
        print("Current live feed from both cameras")

    def testVision(self):
        """Use this function when testing the robot visual input from cameras"""
        print("Begin Test")
        self.activate()
        time.sleep(1)
        self.livefeed()
        time.sleep(1)
        self.shutdown()
        print("End Test")
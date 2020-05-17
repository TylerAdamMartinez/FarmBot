"""
Hands.py created by Tyler Adam Martinez: 
    Created: May 17, 2020
    Last Updated: May 17, 2020

Robot Hands Design (Current plan as of May 17, 2020):
    1     Fingers
    [ ]   Palm
    (R)   Hand Name

      front side
    1111      1111 
(L) [  ]1    1[  ] (R)
      |        |
      
"""

import RPi.GPIO as GPIO
import time

class Hand: 
    """This Class defines all the CV functions for the robot"""
    def right(self):
        """This code for the right hand"""
        print("right hand")
        

    def left(self):
        """This code for the left hand"""
        print("left hand")
        

    def testHands(self):
        """Use this function when testing the robot hands movements"""
        print("Beign test")
        self.right()
        time.sleep(2)
        self.left()
        time.sleep(2)
        print("End of test")



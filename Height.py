"""
Height.py created by Tyler Adam Martinez: 
    Created: May 17, 2020
    Last Updated: May 17, 2020

Robot Adjustable Height Design (Current plan as of May 17, 2020):
    [ ]  Hydrolic pump

    Top

    Face Screen here
    CV Module here
     |
    [ ]
     |
    Main Computer here
    Motor Train here
    
"""

import RPi.GPIO as GPIO
import time

class Height: 
    """This Class defines all the Height Movement functions for the robot"""
    def GotoDefaultHeight(self):
        """This code will automatically adjust the height to its orginal position"""
        print("Returning to Default height")
        time.sleep(2)
        print("At Default height")
        

    def CurrentHeight(self):
        """This code will give the current height of the robot"""
        height = 10
        print("The current height is " + height)

    def MoveUP(self):
        """This code will Move the Robot Up"""
        print("Robot moving up")
        
    def MoveDOWN(self):
        """This code will Move the Robot Up"""
        print("Robot moving down")           

    def testHeightMovement(self):
        """Use this function when testing the robot height movement"""
        print("Current live feed from both cameras")
        self.MoveUP()
        time.sleep(5)
        self.MoveDOWN()
        time.sleep(10)
        self.GotoDefaultHeight()



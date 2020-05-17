"""
Temperature.py created by Tyler Adam Martinez: 
    Created: May 17, 2020
    Last Updated: May 17, 2020

Description:

      
"""

import RPi.GPIO as GPIO
import time

class Temperature: 
    """This Class defines all the Temperature Control functions for the farm"""
    def increase(self):
        """This code for the increase the temperature of the farm"""
        print("Heating up the farm")
        

    def decrease(self):
        """This code for the decrease the temperature of the farm"""
        print("cooling down the farm")
        

    def testTemperatureControl(self):
        """Use this function when testing the robot hands movements"""
        print("Beign test")
        self.increase()
        time.sleep(2)
        self.decrease()
        time.sleep(2)
        print("End of test")

"""
Humidity.py created by Tyler Adam Martinez: 
    Created: May 17, 2020
    Last Updated: May 17, 2020

Description:

      
"""

import RPi.GPIO as GPIO
import time

class Humidity: 
    """This Class defines all the Humidity Control functions for the farm"""
    def increase(self):
        """This code for the increase the Humidity of the farm"""
        print("increase the Humidity of the farm")
        

    def decrease(self):
        """This code for the decrease the Humidity of the farm"""
        print("decrease the Humidity of the farm")
        

    def testHumidityControl(self):
        """Use this function when testing the robot hands movements"""
        print("Beign test")
        self.increase()
        time.sleep(2)
        self.decrease()
        time.sleep(2)
        print("End of test")

"""
Lighting.py created by Tyler Adam Martinez: 
    Created: May 17, 2020
    Last Updated: May 31, 2020

Description:

      
"""

import RPi.GPIO as GPIO
import time



class Lighting: 
    """This Class defines all the Artifical Lighting Control functions for the farm"""
    def __init__(self, Lighting_ctl_pin):
        GPIO.setmode(GPIO.BOARD)
        self.Lighting_ctl_pin = Lighting_ctl_pin
        GPIO.setup(Lighting_ctl_pin, GPIO.OUT)

    def On(self):
        """Use this function to turn on the Artifical Lighting"""
        print("Lights are Currently On")
        GPIO.output(self.Lighting_ctl_pin, GPIO.HIGH)
        

    def Off(self):
        """Use this function to turn off the Artifical Lighting"""
        print("Lights are Currently Off")
        GPIO.output(self.Lighting_ctl_pin, GPIO.LOW)
        

    def Auto(self):
        """Use this function to automatical turn on and off the Artifical Lighting based on the time of day"""
        time_of_day_in_hours = time.gmtime()

        if time_of_day_in_hours[3] > 6 and time_of_day_in_hours[3] < 18:
            self.On()
        else: 
            self.Off()

    def Test(self):
        """Use this function to test if the Artifical Lighting is working. The lights should turn on for 2 seconds then turn back off for another 2 seconds and repeat this process 3 times."""
        print("Start of test")
        for i in range(3):
            print("Current iteration: " , (i + 1))
            self.On()
            time.sleep(2)
            self.Off()
            time.sleep(2)
        print("End of test")


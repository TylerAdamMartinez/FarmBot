"""
Farm.py created by Tyler Adam Martinez: 
    Created: May 17, 2020
    Last Updated: May 17, 2020

Description:

      
"""

import RPi.GPIO as GPIO
import time

class Farm: 
    """This Class defines all the Nutrients and Fertiliser Control functions for the farm"""
    
    def NutrientsIncrease(self):
        """This code for the increase the Humidity of the farm"""
        print("increase the Nutrients Increase of the farm")
            
    def NutrientsDecrease(self):
        """This code for the decrease the Humidity of the farm"""
        print("decrease the Nutrients Decrease of the farm")

    def testNutrients(self):
        self.NutrientsIncrease()
        time.sleep(2)
        self.NutrientsDecrease()
        time.sleep(2)
        
    def FertiliserIncrease(self):
        """This code for the increase the Humidity of the farm"""
        print("increase the Fertiliser Increase  of the farm")
        
    def FertiliserDecrease(self):
        """This code for the decrease the Humidity of the farm"""
        print("decrease the Fertiliser Decrease of the farm")

    def testFertiliser(self):
        self.FertiliserIncrease()
        time.sleep(2)
        self.FertiliserDecrease()
        time.sleep(2)
    
    def testFarmControl(self):
        """Use this function when testing the robot hands movements"""
        print("Beign test")
        self.testNutrients()
        time.sleep(2)
        self.testFertiliser()
        print("End of test")
"""
Lighting.py created by Tyler Adam Martinez: 
    Created: May 17, 2020
    Last Updated: May 17, 2020

Description:

      
"""

#import RPi.GPIO as GPIO
import time

class Lighting: 
    """This Class defines all the Artifical Lighting Control functions for the farm"""
    
    def IncreaseRED(self):
        """This code for the increase the Red Lighting of the farm"""
        print("increase the Red Lighting of the farm")
        

    def DecreaseRED(self):
        """This code for the decrease theRed Lighting of the farm"""
        print("decrease the Red Lighting of the farm")
    
    def testREDLighting(self):
        """Use this function when testing the robot hands movements"""
        print("Beign test")
        self.IncreaseRED()
        time.sleep(2)
        self.DecreaseRED()
        time.sleep(2)
        print("End of test")

    def IncreaseBLUE(self):
        """This code for the increase the Blue Lighting of the farm"""
        print("increase the Blue Lighting of the farm")
        

    def DecreaseBLUE(self):
        """This code for the decrease the Blue Lighting of the farm"""
        print("decrease the Blue Lighting of the farm")
    
    def testBLUELighting(self):
        """Use this function when testing the robot hands movements"""
        print("Beign test")
        self.IncreaseBLUE()
        time.sleep(2)
        self.IncreaseBLUE()
        time.sleep(2)
        print("End of test")


    def testArtificalLightingControl(self):
        """Use this function when testing the robot hands movements"""
        print("Beign test")
        self.testREDLighting()
        time.sleep(2)
        self.testBLUELighting()
        print("End of test")
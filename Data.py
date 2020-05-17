"""
Data.py created by Tyler Adam Martinez: 
    Created: May 17, 2020
    Last Updated: May 17, 2020


This Class will give all the Data for the other class and put into nice graphs and charts    
"""

import matplotlib.pyplot as plt
import matplotlib as mat
import numpy as np
import scipy as sp
import pylab as lab
from math import pi
import math

class Data: 
    """This Class defines all the Visual Data functions for the robot"""
    def plot(self):
        """This code for ploting the outputs of parts of the robot"""
        def Movement():
            print("Now plotting the Horizontal Movement of the Robot")

            direction = 0 # this should be input from the Movement.py
            turn = 0 # this should be input from the Movement.py

            plt.figure(1)
            plt.title('Horizontal Movement Plot')
            plt.ylabel('Forward - Backward')
            plt.xlabel('Left - Right')
            plt.plot(direction, turn)

            plt.show()

        def Height():
            print("Now plotting the Virtical Movement of the Robot")

            currentHeight = 0 # this should be input from the Movement.py
            
            plt.figure(1)
            plt.title('Virtical Movement Plot')
            plt.ylabel('Up - Down')
            plt.plot(currentHeight)

            plt.show()           
        
        def Hands():
            print("Now plotting the Hands Movement of the Robot")

            direction = 0 # this should be input from the Movement.py
            turn = 0 # this should be input from the Movement.py

            plt.figure(1)
            plt.title('Horizontal Movement Plot')
            plt.ylabel('Forward - Backward')
            plt.xlabel('Left - Right')
            plt.plot(direction, turn)

            plt.show()





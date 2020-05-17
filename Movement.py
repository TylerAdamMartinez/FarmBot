"""
Movement.py created by Tyler Adam Martinez: 
    Created: May 16, 2020
    Last Updated: May 17, 2020

Robot Drive Train Design:
    @     Center of Gravity of the Robot
    ||-   Wheels controlled by DC Motor for movement
    +     Rollies wheels for stability
    (A)   Motor Name

     front side  
       +---+
       |   |
 (A) ||- @ -|| (B)
       |   | 
       --+--

Motor Controller System:
    Dual Motor H-Bridge system      
"""

import RPi.GPIO as GPIO
import time

#pins for the Motor A
enA_PWM0 = 12 
in1A = 16
in2A = 18
#pins for the Motor B
enB_PWM1 = 33 
in1B = 31
in2B = 29

#intiallizing other useful varibles
dutycycle = 50; # range for pi (0 - 100) for PWM on raspberry pi
#GPIO.setmode(GPIO.BOARD);  


#setting up GPIO pins for Motor A
GPIO.setup(enA_PWM0, GPIO.OUT);
pwmA = GPIO.PWM(enA_PWM0, 1000);
GPIO.setup(in1A, GPIO.OUT);
GPIO.setup(in2A, GPIO.OUT);


#setting up GPIO pins for Motor B
GPIO.setup(enB_PWM1, GPIO.OUT);
pwmB = GPIO.PWM(enB_PWM1, 1000); #The gives a PWM signal of 1000Hz;however, the Ardiuno is 16MHz
GPIO.setup(in1B, GPIO.OUT);
GPIO.setup(in2B, GPIO.OUT);


class Move: 
    """This Class defines all the movement functions for the robot"""
    def fwd(self):
        """This code will make the robot move forward"""
        print("Robot Moving Forward")
        
        GPIO.output(enA_PWM0, GPIO.HIGH);
        GPIO.output(enB_PWM1, GPIO.HIGH);
    
        GPIO.output(in1A, GPIO.HIGH);
        GPIO.output(in2A, GPIO.LOW);
    
        GPIO.output(in1B, GPIO.HIGH);
        GPIO.output(in2B, GPIO.LOW);
        
    
    
    def bwd(self):
        """This code will make the robot move backwards"""
        print("Robot Moving Backwards")
        
        GPIO.output(enA_PWM0, GPIO.HIGH)
        GPIO.output(enB_PWM1, GPIO.HIGH)
    
        GPIO.output(in1A, GPIO.LOW)
        GPIO.output(in2A, GPIO.HIGH)
    
        GPIO.output(in1B, GPIO.LOW)
        GPIO.output(in2B, GPIO.HIGH)
        
    
    def spinright(self):
        """This code will make the robot spin right"""
        print("Robot Spinning Right")
        
        GPIO.output(enA_PWM0, GPIO.HIGH)
        GPIO.output(enB_PWM1, GPIO.HIGH)
    
        GPIO.output(in1A, GPIO.LOW)
        GPIO.output(in2A, GPIO.HIGH)
    
        GPIO.output(in1B, GPIO.HIGH)
        GPIO.output(in2B, GPIO.LOW)
        

    def spinleft(self):
        """This code will make the robot spin left"""
        print("Robot Spinning Left")
        
        GPIO.output(enA_PWM0, GPIO.HIGH)
        GPIO.output(enB_PWM1, GPIO.HIGH)
    
        GPIO.output(in1A, GPIO.HIGH)
        GPIO.output(in2A, GPIO.LOW)
    
        GPIO.output(in1B, GPIO.LOW)
        GPIO.output(in2B, GPIO.HIGH)
        

    def left(self):
        """This code will make the robot turn left"""
        print("Robot Turning Left")
        
        pwmA.start(dutycycle)
        GPIO.output(enB_PWM1, GPIO.HIGH)
    
        GPIO.output(in1A, GPIO.HIGH)
        GPIO.output(in2A, GPIO.LOW)
    
        GPIO.output(in1B, GPIO.HIGH)
        GPIO.output(in2B, GPIO.LOW)
    
        pwmA.stop()
        
    
    def right(self):
        """This code will make the robot turn right"""
        print("Robot Turning Right")
        
        GPIO.output(enA_PWM0, GPIO.HIGH)
        pwmB.start(dutycycle)
    
        GPIO.output(in1A, GPIO.HIGH)
        GPIO.output(in2A, GPIO.LOW)
    
        GPIO.output(in1B, GPIO.HIGH)
        GPIO.output(in2B, GPIO.LOW)
    
        pwmB.stop()
        

    def mstop(self):
        """This code will make the robot stop moving"""
        print("Robot Stopping")
        
        GPIO.output(enA_PWM0, GPIO.LOW)
        GPIO.output(enB_PWM1, GPIO.LOW)

        print("Robot Stopped")
        

    def testMotors(self):
        """Use this function when testing the robot movement ablility"""
        print("Begin Motor Movement Test")
        self.fwd()
        time.sleep(5)
        self.mstop()
        time.sleep(5)
        self.left()
        time.sleep(5)
        self.right()
        time.sleep(5)
        self.bwd()
        time.sleep(5)
        self.spinright()
        time.sleep(5)
        self.spinleft()
        time.sleep(5)
        print("Finish Motor Movement Test");
     

#Safe termination of program
pwmA.stop(); pwmB.stop();
#GPIO reset to normal state after termination of program
GPIO.cleanup();

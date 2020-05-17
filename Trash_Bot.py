#include files for Robot
import gym #OpenAI API
import Movement  
import Data
import Vision
import Height
import Hands


#include files for Verical Farm
import Farm
import Temperture
import Humidity
import Lighting




print("Hello, I'm Andros")

#Objects for the Robot
CV = Vision.Vision()
Height = Height.Height()
Hands = Hands.Hand()

def testRobot():
    CV.testVision()
    Height.testHeightMovement()
    Hands.testHands()


#Objects for the Farm
Farm = Farm.Farm()
Temp = Temperture.Temperature()
Humdit = Humidity.Humidity()
Lights = Lighting.Lighting()

def testFarm():
    Farm.testFarmControl()
    Temp.testTemperatureControl()
    Humdit.testHumidityControl()
    Lights.testArtificalLightingControl()

testRobot()
testFarm()
import Movement  
import Data
import Vision
import Height
import Hands
import gym #OpenAI API


print("Hello, I'm Andros")

CV = Vision.Vision()

CV.activate()
CV.livefeed()
CV.shutdown()

Height = Height.Height()

Height.testHeightMovement()

Hands = Hands.Hand()
Hands.testHands()
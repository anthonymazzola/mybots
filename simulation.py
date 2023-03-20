import pybullet as p
import constants as c
import time
import numpy
import pybullet_data
import pyrosim.pyrosim as pyrosim
from world import WORLD
from robot import ROBOT

class SIMULATION:

    def __init__(self, directOrGui):
        
        self.directOrGUI = directOrGui
        
        if self.directOrGui == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        elif directOrGui == "GUI":
            self.physicsClient = p.connect(p.GUI)
        
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()
        
        
    def Run(self):
        
        for x in range(1000):
            
            p.stepSimulation()
            
            self.robot.Sense(x)
            
            self.robot.Think()
            
            self.robot.Act(x)
        
            if self.directOrGui == "GUI":
                time.sleep(1/240)
    
    def Get_Fitness(self):
        self.robot.Get_Fitness()
            
    def __del__(self):

        p.disconnect()
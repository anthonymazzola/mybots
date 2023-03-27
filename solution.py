import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c

class SOLUTION:
    
    def __init__(self, ID):
        self.ID = ID        
        self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        self.weights = self.weights * 2 - 1
        
    def Evaluate(self, directOrGui):
        pass
    
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[3,3,0.5] , size=[1,1,1])    
        pyrosim.End()
        
    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [0.0,-0.5,1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="Backleg", pos=[0.0,-0.5,0.0] , size=[0.2,1,0.2])
        pyrosim.Send_Joint( name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [0.0,0.5,1.0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="Frontleg", pos=[0.0,0.5,0.0] , size=[0.2,1,0.2])
        pyrosim.Send_Joint( name = "Torso_Leftleg" , parent= "Torso" , child = "Leftleg" , type = "revolute", position = [-0.5,0.0,1.0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="Leftleg", pos=[-0.5,0.0,0.0] , size=[1.0,0.2,0.2])
        pyrosim.Send_Joint( name = "Torso_Rightleg" , parent= "Torso" , child = "Rightleg" , type = "revolute", position = [0.5,0.0,1.0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="Rightleg", pos=[0.5,0.0,0.0] , size=[1.0,0.2,0.2])
        
        pyrosim.Send_Joint( name = "Frontleg_LowerFrontleg" , parent= "Frontleg" , child = "LowerFrontleg" , type = "revolute", position = [0,1,0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerFrontleg", pos=[0.0,0.0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "Backleg_LowerBackleg" , parent= "Backleg" , child = "LowerBackleg" , type = "revolute", position = [0,-1,0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerBackleg", pos=[0.0,0.0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "Leftleg_LowerLeftleg" , parent= "Leftleg" , child = "LowerLeftleg" , type = "revolute", position = [-1,0,0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerLeftleg", pos=[0.0,0.0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "Rightleg_LowerRightleg" , parent= "Rightleg" , child = "LowerRightleg" , type = "revolute", position = [1,0,0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerRightleg", pos=[0.0,0.0,-0.5] , size=[0.2,0.2,1])
        pyrosim.End()
        
    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.ID) + ".nndf")
        
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "LowerFrontleg")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "LowerBackleg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LowerLeftleg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LowerRightleg")
        
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_Frontleg")
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_Backleg")
        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_Leftleg")
        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_Rightleg")
        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "Frontleg_LowerFrontleg")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Backleg_LowerBackleg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Leftleg_LowerLeftleg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Rightleg_LowerRightleg")
        
        #pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = -1.0 )
        #pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -1.0 )
        #pyrosim.Send_Synapse( sourceNeuronName=0, targetNeuronName=4, weight=-1.0 )
        #pyrosim.Send_Synapse( sourceNeuronName=2, targetNeuronName=4, weight=-1.0 )
        
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow, targetNeuronName = currentColumn+c.numSensorNeurons, weight = self.weights[currentRow][currentColumn])
        
        pyrosim.End()
        
    def Mutate(self):
        randRow = random.randint(0, c.numSensorNeurons - 1)
        randCol = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randRow][randCol] = random.random() * 2 - 1
        
    def Set_ID(self, ID):
        self.ID = ID       
        
    def Start_Simulation(self, directOrGui):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        
        os.system("python3 simulate.py " + directOrGui + " " + str(self.ID) + " 2&>1 &")
        
    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.ID) + ".txt"):

            time.sleep(0.01)
        
        f = open("fitness" + str(self.ID) + ".txt", "r")
        self.fitness = float(f.read())
        f.close()
        os.system("rm fitness" + str(self.ID) + ".txt")
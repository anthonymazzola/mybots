import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import time

class SOLUTION:
    
    def __init__(self, ID):
        self.ID = ID        
        self.weights = numpy.random.rand(3,2)
        self.weights = self.weights * 2 - 1
        
    def Evaluate(self, directOrGui):
        pass
    
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[3,3,0.5] , size=[1,1,1])    
        pyrosim.End()
        
    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [-0.5,0.0,1])
        pyrosim.Send_Cube(name="Backleg", pos=[-0.5,0,-0.5] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [0.5,0,1.0])
        pyrosim.Send_Cube(name="Frontleg", pos=[0.5,0,-0.5] , size=[1,1,1])
        pyrosim.End()
        
    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.ID) + ".nndf")
        
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")
        
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_Backleg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_frontleg")
        
        #pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = -1.0 )
        #pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -1.0 )
        #pyrosim.Send_Synapse( sourceNeuronName=0, targetNeuronName=4, weight=-1.0 )
        #pyrosim.Send_Synapse( sourceNeuronName=2, targetNeuronName=4, weight=-1.0 )
        
        for currentRow in {0, 1, 2}:
            for currentColumn in {0, 1}:
                pyrosim.Send_Synapse( sourceNeuronName = currentRow, targetNeuronName = currentColumn+3, weight = self.weights[currentRow][currentColumn])
        
        pyrosim.End()
        
    def Mutate(self):
        randRow = random.randint(0, 2)
        randCol = random.randint(0, 1)
        self.weights[randRow][randCol] = random.random() * 2 - 1
        
    def Set_ID(self, ID):
        self.ID = ID       
        
    def Start_Simulation(self, directOrGui):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        
        os.system("python3 simulate.py " + directOrGui + " " + str(self.ID) + " &")
        
    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.ID) + ".txt"):

            time.sleep(0.01)
        
        f = open("fitness" + str(self.ID) + ".txt", "r")
        self.fitness = float(f.read())
        f.close()
        os.system("rm fitness" + str(self.ID) + ".txt")
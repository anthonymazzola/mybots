import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = numpy.zeros(1000)
        self.Prepare_To_Act()
        
    def Prepare_To_Act(self):
        
        self.amplitude = c.backLegAmplitude
        self.frequency = c.backLegFrequency
        self.offset = c.backLegPhaseOffset
        
        for i in range(1000):
            if self.jointName == "Torso_Frontleg":
                self.motorValues = self.amplitude * numpy.sin(self.frequency * c.array + self.offset)
            elif self.jointName == "Torso_Backleg":
                self.motorValues = self.amplitude * numpy.sin(0.5*self.frequency * c.array + self.offset)
                
    def Set_Value(self, robot, desiredAngle):
        pyrosim.Set_Motor_For_Joint(

        bodyIndex = robot,

        jointName = self.jointName,

        controlMode = p.POSITION_CONTROL,

        targetPosition = desiredAngle,

        maxForce = c.maxForce)
    
    def Save_Values(self):
        numpy.save('data/motorValues.npy', self.motorValues)
    
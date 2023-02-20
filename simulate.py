import pybullet as p
import numpy
import random
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time

backLegAmplitude = numpy.pi/4
backLegFrequency = 4
backLegPhaseOffset = 0
frontLegAmplitude = numpy.pi/2
frontLegFrequency = 12
frontLegPhaseOffset = numpy.pi/4

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

array = numpy.linspace(0, 360, 1000)
backArrayValues = backLegAmplitude * numpy.sin(backLegFrequency * array + backLegPhaseOffset)
frontArrayValues = frontLegAmplitude * numpy.sin(frontLegFrequency * array + frontLegPhaseOffset)
#numpy.save('data/arrayrValues.npy', arrayValues)


for x in range(1000):
    p.stepSimulation()
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
    pyrosim.Set_Motor_For_Joint(

bodyIndex = robotId,

jointName = "Torso_Backleg",

controlMode = p.POSITION_CONTROL,

targetPosition = backArrayValues[x],

maxForce = 100)
    pyrosim.Set_Motor_For_Joint(

bodyIndex = robotId,

jointName = "Torso_Frontleg",

controlMode = p.POSITION_CONTROL,

targetPosition = frontArrayValues[x],

maxForce = 100)
    time.sleep(1/240)
numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
p.disconnect()

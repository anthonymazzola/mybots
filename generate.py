import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0.0
y= 0.0
z = 0.5

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])    
    pyrosim.End()

Create_World()
import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0.0
y= 0.0
z = 1.5

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[3,3,z] , size=[length,width,height])    
    pyrosim.End()
    
def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[x,y,z] , size=[length,width,height])
    pyrosim.Send_Joint( name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [-0.5,0.0,1])
    pyrosim.Send_Cube(name="Backleg", pos=[-0.5,0,-0.5] , size=[length,width,height])
    pyrosim.Send_Joint( name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [0.5,0,1.0])
    pyrosim.Send_Cube(name="Frontleg", pos=[0.5,0,-0.5] , size=[length,width,height])
    pyrosim.End()

Create_World()
Create_Robot()
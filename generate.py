import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0.0
y= 0.0
z = 0.5

i = 0
j = 0
k = 0

pyrosim.Start_SDF("boxes.sdf")
while k < 5:
    j = 0
    while j < 5:
        i = 0
        length = 1
        width = 1
        height = 1
        while i < 10:
            pyrosim.Send_Cube(name="Box", pos=[x+j,y+k,z+i] , size=[length,width,height])
            i += 1
            length *= .9
            width *= .9
            height *= .9
        j += 1
    k += 1
    
pyrosim.End()

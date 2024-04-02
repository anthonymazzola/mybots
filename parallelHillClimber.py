from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        
        
    def Evolve(self):
        self.Evaluate(self.parents)       
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        
            
    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()
        
        self.Print()

        self.Select()
        
        
    def Spawn(self):
        self.children = {}
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
    
    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()
    
    def Select(self):
        for i in self.parents:
            if self.children[i].fitness < self.parents[i].fitness:
                self.parents[i] = self.children[i]
    
    def Show_Best(self):
        best = 1.0
        for i in self.parents:
            if self.parents[i].fitness < best:
                best = self.parents[i].fitness
                best_key = i
        self.parents[best_key].Start_Simulation("GUI")
    
    def Print(self):
        print("\n")
        for i in self.parents:
            print("Parent: " + str(self.parents[i].fitness) + ", Child:" + str(self.children[i].fitness) )
        print("\n")
    
    def Evaluate(self, solutions):
        for x in solutions:
            solutions[x].Start_Simulation("DIRECT")
        for x in solutions:
            solutions[x].Wait_For_Simulation_To_End()
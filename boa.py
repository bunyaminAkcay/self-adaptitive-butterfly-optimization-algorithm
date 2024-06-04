import numpy as np
import random
from objective_function import ObjectiveFunction
from stopping_criteria import StoppingCriteria
from base_boa import BaseBOA

class ButterflyOptimizationAlgorithm(BaseBOA):

    def __init__(self, objectiveFunction : ObjectiveFunction, stoppingCriteria : StoppingCriteria, populationSize, c, aMin, aMax, p, generatePlotData = False):
        BaseBOA.__init__(self, objectiveFunction, stoppingCriteria, populationSize, p, generatePlotData)
        self.__c = c
        self.__aMin = aMin
        self.__aMax = aMax
        self.__a = aMin
        self.__generateInitialPopulation()

    
    def __generateInitialPopulation(self):
        bounds = self._objectiveFunction.getBounds()
        dimension = self._objectiveFunction.getDimension()
        
        for i in range(self._populationSize):
            position = []
            for j in range(dimension):
                position.append(random.uniform(bounds[0], bounds[1]))
            positionArray = np.array(position)
            self._positions.append(positionArray)

            fitness = self._objectiveFunction.evaluate(positionArray)
            if (self._bestFitness == None or self._bestFitness > fitness):
                self._bestFitness = fitness
                self._bestPosition = positionArray
    
    def run(self):
        while self._stoppingCriteria.checkCriteria() == False:
            for i in range(self._populationSize):
                I = self._objectiveFunction.evaluate(self._positions[i])
                fragrance = self.__c * I**self.__a
                r = random.uniform(0,1)
                
                if (r < self._p):
                    self._positions[i] = self._positions[i] + (r**2 * self._bestPosition - self._positions[i]) * fragrance
                    self._checkBoundaries(self._positions[i])
                else:
                    j = random.randint(0, self._populationSize -1)
                    k = random.randint(0, self._populationSize -1)
                    self._positions[i] = self._positions[i] + ( r**2 * self._positions[j] - self._positions[k]) * fragrance
                    self._checkBoundaries(self._positions[i])
                
                f = self._objectiveFunction.evaluate(self._positions[i])
                
                if  f < self._bestFitness:
                    self._bestFitness = f
                    self._bestPosition = self._positions[i]

            self.__a = self.__aMin + (self.__aMax - self.__aMin) * self._stoppingCriteria.getProgress()
            self._addGraphData()

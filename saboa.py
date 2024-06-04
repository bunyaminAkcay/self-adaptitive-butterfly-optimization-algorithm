import numpy as np
import random
from objective_function import ObjectiveFunction
from stopping_criteria import StoppingCriteria
from base_boa import BaseBOA

class SelfAdaptiveButterflyOptimizationAlgorithm(BaseBOA):

    def __init__(self, objectiveFunction : ObjectiveFunction, stoppingCriteria : StoppingCriteria, populationSize, p, generatePlotData = False):
        BaseBOA.__init__(self, objectiveFunction, stoppingCriteria, populationSize, p, generatePlotData)
        self.__worstPosition = None
        self.__worstFitness = None
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
            if (self.__worstFitness == None or self.__worstFitness < fitness):
                self.__worstFitness = fitness
                self.__worstPosition = positionArray
                
    def run(self):
        while self._stoppingCriteria.checkCriteria() == False:
                
            for i in range(self._populationSize):
                u = np.random.standard_normal()
                f = u * (1 - self._stoppingCriteria.getProgress())
                r = random.uniform(0,1)
                if self._p > r:
                    self._positions[i] = self._bestPosition + (self._positions[i] - self._bestPosition)*f
                    self._checkBoundaries(self._positions[i])
                else:
                    self._positions[i] = 0.5 * (self._bestPosition + self.__worstPosition) * f
                    self._checkBoundaries(self._positions[i])

                fitness = self._objectiveFunction.evaluate(self._positions[i])
                
                if  fitness < self._bestFitness:
                    self._bestFitness = fitness
                    self._bestPosition = self._positions[i]
                
                if fitness > self.__worstFitness:
                    self.__worstFitness = fitness
                    self.__worstPosition = self._positions[i]
            
            self._addGraphData()
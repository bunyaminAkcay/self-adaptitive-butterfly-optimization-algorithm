from objective_function import ObjectiveFunction
from stopping_criteria import StoppingCriteria

class BaseBOA:

    def __init__(self, objectiveFunction : ObjectiveFunction, stoppingCriteria : StoppingCriteria, populationSize, p, generateGraphData):
        self._populationSize = populationSize
        self._objectiveFunction = objectiveFunction
        self._stoppingCriteria = stoppingCriteria
        self._bestPosition = None
        self._bestFitness = None
        self._positions = []
        self._p = p
        self._generateGraphData = generateGraphData
        self.__graphDataT = []
        self.__graphDataPositions = []
        self.__graphDataFitness = []
    
    def printResults(self):
        print("=== Results ===")
        print("position:\t" + str(self._bestPosition))
        print("output:\t\t" + str(self._objectiveFunction.evaluate(self._bestPosition)))
    
    def getResult(self):
        if self._stoppingCriteria.checkCriteria():
            return self._objectiveFunction.evaluate(self._bestPosition)
        else:
            return None
    
    def _checkBoundaries(self, position):
        bounds = self._objectiveFunction.getBounds()
        for i in range(len(position)):
            if position[i] < bounds[0]:
                position[i] = bounds[0]
            if position[i] > bounds[1]:
                position[i] = bounds[1]
    
    def _addGraphData(self):
        if self._generateGraphData:
            if len(self.__graphDataFitness) == 0:
                self.__graphDataFitness.append(self._bestFitness)
                self.__graphDataPositions.append(self._bestPosition)
                self.__graphDataT.append(self._stoppingCriteria.getIterationNumber())
            elif self.__graphDataFitness[-1] != self._bestFitness:
                if self.__graphDataT[-1] +1 != self._stoppingCriteria.getIterationNumber():
                    self.__graphDataFitness.append(self.__graphDataFitness[-1])
                    self.__graphDataPositions.append(self.__graphDataPositions[-1])
                    self.__graphDataT.append(self._stoppingCriteria.getIterationNumber() -1)
                self.__graphDataFitness.append(self._bestFitness)
                self.__graphDataPositions.append(self._bestPosition)
                self.__graphDataT.append(self._stoppingCriteria.getIterationNumber())
            elif self._stoppingCriteria.getIterationNumber() == self._stoppingCriteria.getCriteriaValue():
                self.__graphDataFitness.append(self._bestFitness)
                self.__graphDataPositions.append(self._bestPosition)
                self.__graphDataT.append(self._stoppingCriteria.getIterationNumber())

    def getGraphDataT(self):
        return self.__graphDataT
    
    def getGraphDataPositions(self):
        return self.__graphDataPositions

    def getGraphDataFitness(self):
        return self.__graphDataFitness

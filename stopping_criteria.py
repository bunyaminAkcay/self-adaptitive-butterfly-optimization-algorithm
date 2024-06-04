from enum import Enum
from datetime import datetime

class Criteria(Enum):
    maximum_iteration_number = 0
    maximum_cpu_time = 1
    maximum_number_of_iterations_with_no_improvement = 2

class StoppingCriteria():

    def __init__(self, criteria, value):
        self.__iterationNumber = 0
        self.__maxIterationNumber = None
        self.__maxCpuTime = None
        self.__maxNumberOfIterationsWithNoImprovement = None
        self.__startTime = datetime.now()
        self.__passedTime = 0
        self.__criteria = criteria
        self.__value = value
        self.__criteriaFunction = self.__setCriteriaFunction(value)
        

    def __setCriteriaFunction(self, value):
        if self.__criteria == Criteria.maximum_iteration_number:
            self.__maxIterationNumber = value
            return self.__checkMaximumIterationNumber
        elif self.__criteria == Criteria.maximum_cpu_time:
            self.__maxCpuTime = value
            return self.__checkMaximumCpuTime
        elif self.__criteria == Criteria.maximum_number_of_iterations_with_no_improvement:
            return self.__checkMaximumNumberOfIterationsWithNoImprovement
        else:
            AssertionError("Unknown criteria")
    
    def checkCriteria(self):
        result = self.__criteriaFunction()
        self.__iterationNumber += 1
        return result
        
    def getIterationNumber(self):
        return self.__iterationNumber
    
    def getCriteriaValue(self):
        return self.__value

    #0 is simulation have stareted yet, 1 is simulation have finished
    def getProgress(self):
        if self.__criteria == Criteria.maximum_iteration_number:
            return self.__iterationNumber/self.__maxIterationNumber
        elif self.__criteria == Criteria.maximum_cpu_time:
            return self.__passedTime/self.__maxIterationNumber

    def __checkMaximumIterationNumber(self):
        if (self.__iterationNumber > self.__maxIterationNumber):
            return True
        else:
            return False

    def __checkMaximumCpuTime(self):
        self.__passedTime = (datetime.now() - self.__startTime).total_seconds()
        if (self.__passedTime > self.__maxCpuTime):
            return True
        else:
            return False

    def __checkMaximumNumberOfIterationsWithNoImprovement():
        pass
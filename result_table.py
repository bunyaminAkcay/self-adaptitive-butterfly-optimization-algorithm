from saboa import SelfAdaptiveButterflyOptimizationAlgorithm
from boa import ButterflyOptimizationAlgorithm
from stopping_criteria import Criteria, StoppingCriteria
import statistics
import numpy as np
import matplotlib.pyplot as plt

class ResultTable:

    def __init__(self, objectiveFunctions, sampleSize, criteria : Criteria, criteriaValue):
        self.__objectiveFunctions = objectiveFunctions
        self.__criteria = criteria
        self.__sampleSize = sampleSize
        self.__criteriaValue = criteriaValue
        self.__boaResults = {}
        self.__saboaResults = {}
        self.__boaFitnesses = {}
        self.__saboaFitnesses = {}
        
    

    def calculateTable(self):
        total = 1
        size = len(self.__objectiveFunctions) * self.__sampleSize * 2  
        
        index = 0
        for f in self.__objectiveFunctions:
            index += 1
            fmin = f.getMin()

            if fmin == None:
                continue

            bestFitnessOfBoa = []
            bestFitnessOfSaboa = []

            for i in range(self.__sampleSize):
                criteria = StoppingCriteria(self.__criteria, self.__criteriaValue)
                saboa = SelfAdaptiveButterflyOptimizationAlgorithm(f, criteria, 50, 0.8)
                saboa.run()
                bestFitnessOfSaboa.append(saboa.getResult())
                print(str(total) + "/" + str(size))
                total +=1

            for i in range(self.__sampleSize):
                criteria = StoppingCriteria(self.__criteria, self.__criteriaValue)
                boa = ButterflyOptimizationAlgorithm(f, criteria, 50, 0.01, 0.1, 0.3, 0.8)
                boa.run()
                bestFitnessOfBoa.append(boa.getResult())
                print(str(total) + "/" + str(size))
                total +=1

            self.__saboaResults["f"+ str(index)] = self.__getResultFromFitness(bestFitnessOfSaboa, fmin)
            self.__boaResults["f"+ str(index)] = self.__getResultFromFitness(bestFitnessOfBoa, fmin)
            
            self.__boaFitnesses["f"+ str(index)] = bestFitnessOfBoa
            self.__saboaFitnesses["f"+ str(index)] = bestFitnessOfSaboa


    def printResults(self):
        print("\n=== BOA Results ===")
        for functionName, values in self.__boaResults.items():
            print(functionName + ": " + str(values))
        print("\n=== SABOA Results ===")
        for functionName, values in self.__saboaResults.items():
            print(functionName + ": " + str(values))
    
    def plotBoxes(self):
        algorithmNames = ["BOA", "SABOA"]
        
        fig, axes = plt.subplots(4, 4, figsize=(12, 16))
        
        
        for i in range(len(self.__boaFitnesses)):
            row = i // 4
            col = i % 4
            values = [self.__boaFitnesses["f"+str(i+1)], self.__saboaFitnesses["f"+str(i+1)]]
            axes[row, col].boxplot(values, patch_artist=True, boxprops=dict(facecolor='blue', color='blue'))

            axes[row, col].set_xticklabels( algorithmNames, rotation=45)
            axes[row, col].set_ylabel(f'f{i+1}')
        
        plt.tight_layout()
        plt.show()

    def __getResultFromFitness(self, fitnessList, fmin):
        best = None
        bestDiff = None
        worst = None
        worstDiff = None

        mean = statistics.mean(fitnessList)
        std = np.std(np.array(fitnessList))

        for fitness in fitnessList:
            diff = abs(fitness - fmin)
            if bestDiff == None or bestDiff > diff:
                bestDiff = diff
                best = fitness
            if worstDiff == None or worstDiff < diff:
                worstDiff = diff
                worst = fitness
        
        return (best, worst, mean, std)

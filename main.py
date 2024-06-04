from objective_function import ObjectiveFunction
from stopping_criteria import *
from result_table import ResultTable
from saboa import SelfAdaptiveButterflyOptimizationAlgorithm
from boa import ButterflyOptimizationAlgorithm
import formula
import matplotlib.pyplot as plt
import numpy as np

def plotSurfacesAndPaths(objectiveFunctions, objectiveFunctions2DBestPositions, criteria, criteriaValue):
    
    for i, objectiveFunction in enumerate(objectiveFunctions):

        bestPositions = objectiveFunctions2DBestPositions[i]
        bestPositionsX = [item[0] for item in bestPositions]
        bestPositionsY = [item[1] for item in bestPositions]
        

        #Butterfly Optimization Algorithm
        stoppingCriteria1 = StoppingCriteria(criteria, criteriaValue)
        stoppingCriteria2 = StoppingCriteria(criteria, criteriaValue)

        boa = ButterflyOptimizationAlgorithm(objectiveFunction, stoppingCriteria1, 50, 0.01, 0.1, 0.3, 0.8, True)
        boa.run()
        
        #Self Adaptive Butterfly Optimization Algorithm
        saboa = SelfAdaptiveButterflyOptimizationAlgorithm(objectiveFunction, stoppingCriteria2, 50, 0.8, True)
        saboa.run()

        ### 3D
        x1 = np.linspace(objectiveFunction.getBounds()[0], objectiveFunction.getBounds()[1], 400)
        x2 = np.linspace(objectiveFunction.getBounds()[0], objectiveFunction.getBounds()[1], 400)
        x1, x2 = np.meshgrid(x1, x2)
        z = formula.functionWithXY(objectiveFunction.getFormula())(x1, x2)

        fig = plt.figure(figsize=(15, 5))

        ax1 = fig.add_subplot(131, projection='3d')
        ax1.plot_surface(x1, x2, z, cmap='viridis')
        ax1.set_title('3-D $f_'+str(i+1)+'$')
        ax1.set_xlabel('$x_1$')
        ax1.set_ylabel('$x_2$')
        ax1.set_zlabel('$f$')

        # === SABOA ===
        saboaPositionsX = [item[0] for item in saboa.getGraphDataPositions()]
        saboaPositionsY = [item[1] for item in saboa.getGraphDataPositions()]

        saboaXLim = [min(saboaPositionsX)-0.5, max(saboaPositionsX)+0.5]
        saboaYLim = [min(saboaPositionsY)-0.5, max(saboaPositionsY)+0.5]

        x1 = np.linspace(saboaXLim[0], saboaXLim[1], 100)
        x2 = np.linspace(saboaYLim[0], saboaYLim[1], 100)
        x1, x2 = np.meshgrid(x1, x2)
        z = formula.functionWithXY(objectiveFunction.getFormula())(x1, x2)
        
        ax2 = fig.add_subplot(132)
        contour = ax2.contour(x1, x2, z, levels=50, cmap='viridis')
        fig.colorbar(contour)
        ax2.set_title('SABOA search path')
        ax2.set_xlabel('$x_1$')
        ax2.set_ylabel('$x_2$')

        
        ax2.set_xlim(saboaXLim)
        ax2.set_ylim(saboaYLim)

        ax2.plot(saboaPositionsX, saboaPositionsY, 'r--', label='path')
        ax2.plot(bestPositionsX, bestPositionsY, 'g+', markersize=10, label='Best solution')

        # === BOA ===
        boaPositionsX = [item[0] for item in boa.getGraphDataPositions()]
        boaPositionsY = [item[1] for item in boa.getGraphDataPositions()]

        boaXLim = [min(boaPositionsX)-0.5, max(boaPositionsX)+0.5]
        boaYLim = [min(boaPositionsY)-0.5, max(boaPositionsY)+0.5]

        x1 = np.linspace(boaXLim[0], boaXLim[1], 400)
        x2 = np.linspace(boaYLim[0], boaYLim[1], 400)
        x1, x2 = np.meshgrid(x1, x2)
        z = formula.functionWithXY(objectiveFunction.getFormula())(x1, x2)
        
        ax3 = fig.add_subplot(133)
        contour = ax3.contour(x1, x2, z, levels=50, cmap='viridis')
        fig.colorbar(contour)
        ax3.set_title('BOA search path')
        ax3.set_xlabel('$x_1$')
        ax3.set_ylabel('$x_2$')
        
        ax3.set_xlim(boaXLim)
        ax3.set_ylim(boaYLim)

        ax3.plot(boaPositionsX, boaPositionsY, 'r--', label='path')
        ax3.plot(bestPositionsX, bestPositionsY, 'g+', markersize=10, label='Best solution')

    plt.tight_layout()
    plt.show()

def plotConvergenceCurves(objectiveFunctions, criteria, criteriaValue):

    fig, axes = plt.subplots(4, 4, figsize=(15, 15))
    yLims = [[0, 4], [0.3979, 5], [0, 5], [0, 1], [-1.9133 ,-1.8], [0, 1], [0, 0.4], [0, 20], [0, 20], [0, 4], [0, 30], [0, 6], [0, 8], [0, 8]];
    
    for i in range(len(objectiveFunctions)):
        row = i // 4
        col = i % 4

        stoppingCriteria1 = StoppingCriteria(criteria, criteriaValue)
        boa = ButterflyOptimizationAlgorithm(objectiveFunctions[i], stoppingCriteria1, 50, 0.01, 0.1, 0.3, 0.8, True)
        boa.run()

        stoppingCriteria2 = StoppingCriteria(criteria, criteriaValue)
        saboa = SelfAdaptiveButterflyOptimizationAlgorithm(objectiveFunctions[i], stoppingCriteria2, 50, 0.8, True)
        saboa.run()
        
        axes[row, col].plot(boa.getGraphDataT(), boa.getGraphDataFitness(), color="green", label='BOA', linewidth=2.5)
        axes[row, col].plot(saboa.getGraphDataT(), saboa.getGraphDataFitness(), color="red", label='SABOA', linewidth=2.5)
        axes[row, col].set_title(f"f{i+1}")
        axes[row, col].set_ylim(yLims[i])
        axes[row, col].set_xlim([0, criteriaValue])
        axes[row, col].legend()
    
    plt.tight_layout()
    plt.show()

def main():
    f1 = ObjectiveFunction(formula.cube_function, 2, [-100, 100], 0)
    f2 = ObjectiveFunction(formula.branin, 2, [-200, 200] , 0.3979)
    f3 = ObjectiveFunction(formula.himmelblau, 2, [-100, 100], 0)
    f4 = ObjectiveFunction(formula.levy13, 2, [-100, 100] , 0)
    f5 = ObjectiveFunction(formula.mccormick, 2, [-2, 2] , -1.9133)
    f6 = ObjectiveFunction(formula.rotated_ellipse01, 2, [-100, 100], 0)
    f7 = ObjectiveFunction(formula.rotated_ellipse02, 2, [-100, 100] , 0)
    f8 = ObjectiveFunction(formula.levy, 30, [-5, 5] , 0)
    f9 = ObjectiveFunction(formula.power_function, 40, [-10, 10], 0)
    f10 = ObjectiveFunction(formula.ackley, 50, [-10, 10], 0)
    f11 = ObjectiveFunction(formula.bent_cigar, 50, [-1, 1], 0)
    f12 = ObjectiveFunction(formula.rotated_ellipse01, 50, [-10, 10], 0)
    f13 = ObjectiveFunction(formula.sum_squares, 50, [-10, 10], 0)
    f14 = ObjectiveFunction(formula.sum_of_different_powers, 50, [-2, 2], 0)

    objectiveFunctions = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14]
    objectiveFunctions2D = [f1, f2, f3, f4, f5, f6, f7]
    objectiveFunctions2DBestPositions = [[[1, 1]], [[9.42478, 2.475], [-np.pi, 12.275], [np.pi, 2.275] ], [[3,2], [-2.805118, 3.131312], [-3.77931, -3.283186], [3.584428,-1.848126]], [[1,1]], [[-0.54719, -1.54719]], [[0,0]], [[0,0]]]
    
    resultTable = ResultTable(objectiveFunctions, 20, Criteria.maximum_iteration_number, 500)
    resultTable.calculateTable()
    resultTable.printResults()
    resultTable.plotBoxes()

    plotConvergenceCurves(objectiveFunctions, Criteria.maximum_iteration_number, 500)
    plotSurfacesAndPaths(objectiveFunctions2D, objectiveFunctions2DBestPositions, Criteria.maximum_iteration_number, 500)

def main2():
    
    f1 = ObjectiveFunction(formula.mccormick, 2, [-2, 2], 0)
    stoppingCriteria = StoppingCriteria(Criteria.maximum_iteration_number, 500)
    
    #Butterfly Optimization Algorithm
    boa = ButterflyOptimizationAlgorithm(f1, stoppingCriteria, 50, 0.01, 0.1, 0.3, 0.8)
    boa.run()
    boa.printResults()

    #Self Adaptive Butterfly Optimization Algorithm
    saboa = SelfAdaptiveButterflyOptimizationAlgorithm(f1, stoppingCriteria, 50, 0.8)
    saboa.run()
    saboa.printResults()


if __name__ == "__main__":
    main()
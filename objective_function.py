class ObjectiveFunction():
    
    def __init__(self, formula, dimension, bound, fmin=None):
        self.__formula = formula
        self.__dimension = dimension
        self.__range = bound
        self.__fmin = fmin
    
    def getBounds(self):
        return self.__range
    
    def getDimension(self):
        return self.__dimension
    
    def evaluate(self, value):
        #assert len(value) == self.__dimension, "Dimension of objective function does not match with given value"
        return self.__formula(value)

    def getMin(self):
        return self.__fmin

    def getFormula(self):
        return self.__formula
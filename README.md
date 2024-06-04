# Self-Adaptative Butterfly Optimization Algorithm and Butterfly Optimization Algorithm

This repository includes implementation of butterfly optimization algorithm and self-adaptative butterfly optimization algorithm. It is aimed to repeat the results found in the article of [Fan et al. 2020].

## Dependencies

```
pip install numpy
pip install matplotlib
```

## Experimental results and data	

### Convergence Curves

![alt text](https://github.com/bunyaminAkcay/[self-adaptitive-butterfly-optimization-algorithm]/blob/master/results/convergeCurves.png?raw=true)

### Box plots

![alt text](https://github.com/bunyaminAkcay/[self-adaptitive-butterfly-optimization-algorithm]/blob/master/results/boxes.png?raw=true)

### Paths

![alt text](https://github.com/bunyaminAkcay/self-adaptitive-butterfly-optimization-algorithm/blob/master/results/paths/f1.png?raw=true)

![alt text](https://github.com/bunyaminAkcay/self-adaptitive-butterfly-optimization-algorithm/blob/master/results/paths/f2.png?raw=true)

![alt text](https://github.com/bunyaminAkcay/self-adaptitive-butterfly-optimization-algorithm/blob/master/results/paths/f3.png?raw=true)

![alt text](https://github.com/bunyaminAkcay/self-adaptitive-butterfly-optimization-algorithm/blob/master/results/paths/f4.png?raw=true)

![alt text](https://github.com/bunyaminAkcay/self-adaptitive-butterfly-optimization-algorithm/blob/master/results/paths/f5.png?raw=true)

![alt text](https://github.com/bunyaminAkcay/self-adaptitive-butterfly-optimization-algorithm/blob/master/results/paths/f6.png?raw=true)

![alt text](https://github.com/bunyaminAkcay/self-adaptitive-butterfly-optimization-algorithm/blob/master/results/paths/f7.png?raw=true)

## Issues

1. f8 (Levy) does not converge minimum of levy function that is 0. The article of [Fan et al. 2020] show clearly converges to 0. Reason of this issiu sign a wrong implementation of of SABOA or implementation of Levy function.

2. Figure of f5 boa path does not apper for unknown reason.

## References

- [Arora et al. 2019]:

   Arora S, Singh S (2019) *"Butterfly optimization algorithm: a novel approach for global optimization"*. Soft Computing 23(3):715–734

- [Fan et al. 2020]:

   Fan Y, Shao J, Sun G, et al (2020) *"A self-adaption butterfly optimization algorithm for numerical optimization problems"*. IEEE Access 8:88,026–88,041

from functools import reduce
from math import factorial
import operator

K = 10
X = 4

def evaluate_polynomial(a, x):        
    res = list(map(lambda i,ai: (x**i)*ai, range(0,K), a))
    print (sum(res))
    return 0

evaluate_polynomial([1/factorial(x) for x in range(0, K)], X)
# For K=10 and X=4, should print: 54.15414462081129

#Question(Hauk): where to use reduce() func?
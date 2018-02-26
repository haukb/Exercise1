import random
N = 100000

x = [random.random() for a in range(N)]
y = [random.random() for a in range(N)]

pi = (4/N) * [(a**2 + b**2)<1 for a, b in zip(x,y)].count(1)

print (pi)
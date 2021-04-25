import numpy as np
def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

def gamma(n):
    p = 1
    for i in range(1, 100000):
        a = (1/(1+(n/i)))*np.exp(n/i)
        p *= a
    b = (1/n)*np.exp(-0.5772*n)
    return b*p

n_type = str(input("Is your number a float (f) or an integer (i)? "))
if n_type in {'i', 'int', 'integer'}:
    x = int(input("What is your integer? "))
    print(f"{x} factorial = {fact(x)}")
elif n_type in {'f', 'float'}:
    x = float(input("What is your float? "))
    print(f"{x} factorial is {gamma(x+1)}")
else:
    print(f"Input of type {n_type} is not supported")

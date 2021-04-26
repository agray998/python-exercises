import numpy as np
# Defining integer factorial function
def fact(n):
    if n == 0: # base case
        return 1
    return n*fact(n-1) # recursive evaluation

# Defining gamma function
def gamma(n):
    p = 1 # Initialising 'infinite' product
    for i in range(1, 100000): # Generating series terms, calculating series product
        a = (1/(1+(n/i)))*np.exp(n/i)
        p *= a
    b = (1/n)*np.exp(-0.5772*n) # Calculating constant (for given n) factor
    return b*p

# Taking user inputs (number type, number) and calculating fact(int) or gamma(float+1)
n_type = str(input("Is your number a float (f) or an integer (i)? "))
if n_type in {'i', 'int', 'integer'}:
    x = int(input("What is your integer? "))
    print(f"{x} factorial = {fact(x)}")
elif n_type in {'f', 'float'}:
    x = float(input("What is your float? "))
    print(f"{x} factorial is {gamma(x+1)}")
else:
    print(f"Input of type {n_type} is not supported")

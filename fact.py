import numpy as np
n_type = str(input("Is your number a float or an integer? "))
if n_type == "int":
    x = int(input("What is your integer? "))

    def fact(n):
        if n == 1:
            return 1
        return n*fact(n-1)
    print(f"x factorial = {fact(x)}")
else:
    x = float(input("What is your float? "))

    def gamma(n):
        p = 1
        for i in range(1, 100000):
            a = (1/(1+(n/i)))*np.exp(n/i)
            p *= a
        b = (1/n)*np.exp(-0.5772*n)
        return b*p
    print(f"factorial of x is {gamma(x+1)}")

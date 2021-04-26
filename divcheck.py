def divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

u_num1 = int(input("What is your first number? "))
u_num2 = int(input("What is your second number? "))
print(f"{u_num1} is divisible by {u_num2} is {divisible(u_num1, u_num2)}")

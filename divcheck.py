u_num1 = int(input("What is your first number? "))
u_num2 = int(input("What is your second number? "))
if u_num1 % u_num2 == 0 and u_num2 == 2:
    print(f"{u_num1} is even")
elif u_num1 % u_num2 == 0:
    print(f"{u_num1} is divisible by {u_num2}")
else:
    print(f"{u_num1} is not divisible by {u_num2}")

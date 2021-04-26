def isawesome(name):
    string = f"{name} is awesome!"
    return string

i = 0
while i<5:
    u_name = str(input("What is your name? "))
    print(isawesome(u_name))
    i+=1

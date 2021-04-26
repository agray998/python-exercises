u_name = str(input("What is your name? "))
print(f"Hello, {u_name}!")
cmd = "start"
while cmd != 'quit':
    cmd = str(input("What would you like to do? "))
    exec(cmd)

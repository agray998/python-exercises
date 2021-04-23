list_len = int(input("How many elements are in your list? "))
u_list = []
for i in range(0, list_len):
    u_list.append(float(input(f"What is the {i}th element of your list? ")))

bound = float(input("What do you want to search for numbers less than? "))

new_list = [x for x in u_list if x < bound]
print(new_list)

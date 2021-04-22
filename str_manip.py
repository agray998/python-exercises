u_string = str(input("What is your string? "))
l_str = len(u_string)
if l_str > 7 and l_str % 2 == 1:
    a = int((l_str-3)/2)
    mid = u_string[a:(a+3)]
    print(mid)
    new_str = u_string[0:a] + mid.upper() + u_string[a+3:]
    print(new_str)
else:
    print("String must be of odd length and have more than 7 characters")

def grade_calc(h, a, f):
    percent = (h + a + f)*100/175
    print(f"You scored {percent}%")
    bound = {80: 'A', 70: 'B', 60: 'C', 50: 'D'}
    for x in bound:
        
        if percent > x:
            grade = bound[x]
            print(f"Your grade is {grade}")
            break
        
        else:
            continue
    else:
        print("Sorry, you did not pass")


h_score = int(input("What is your homework score? "))
if h_score < 0 or h_score > 25:
    print("Invalid score")
    h_score = int(input("What is your homework score? "))
else:
    pass

a_score = int(input("What is your assessment score? "))
if a_score < 0 or a_score > 50:
    print("Invalid score")
    a_score = int(input("What is your assessment score? "))
else:
    pass

f_score = int(input("What is your final exam score? "))
if f_score < 0 or f_score > 100:
    print("Invalid score")
    f_score = int(input("What is your final exam score? "))
else:
    pass

grade_calc(h_score, a_score, f_score)


        

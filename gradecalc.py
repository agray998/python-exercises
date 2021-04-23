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
        print("Fail")


h_score = int(input("What is your homework score? "))
a_score = int(input("What is your assessment score? "))
f_score = int(input("What is your final exam score? "))

grade_calc(h_score, a_score, f_score)


        

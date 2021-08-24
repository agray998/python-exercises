# Defining percentage and grade calculation procedure
def grade_calc(h, a, f):
    percent = (h + a + f)*100/175
    bound = {80: 'A', 70: 'B', 60: 'C', 50: 'D'}
    for x in bound:
        if percent > x:
            grade = bound[x]
            return f"You scored {percent}%\nYour grade is {grade}"
            break
        else:
            continue
    else:
        return f"You scored {percent}%\nSorry, you did not pass"
valid_score = False
while !valid_score:
# User input homework score
    h_score = int(input("What is your homework score? "))
    if h_score < 0 or h_score > 25: # Check for validity of score
        print("Invalid score")
    else:
        valid_score = True

valid_score = False
while !valid_score:
# User input assessment score
    a_score = int(input("What is your assessment score? "))
    if a_score < 0 or a_score > 50: # Check for validity of score
        print("Invalid score")
    else:
        valid_score = True

valid_score = False
while !valid_score:
# User input final exam score
    f_score = int(input("What is your final exam score? "))
    if f_score < 0 or f_score > 100: # Check for validity of score
        print("Invalid score")
    else:
        valid_score = True

# Call grade_calc function with user inputs as arguments
print(grade_calc(h_score, a_score, f_score))


        

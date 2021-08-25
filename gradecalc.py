# Defining percentage and grade calculation function
def grade_calc(h, a, f):
    percent = int((h + a + f) * 100 / 175)
    bounds = {100: 'A*', 90: 'A*', 80: 'A', 70: 'B', 60: 'C', 50: 'D'}
    bound = percent - (percent % 10)
    grade = bounds.get(bound, "Fail")
    return f"You scored {percent}%. Your grade is {grade}"

valid_score = False
while valid_score == False:
# User input homework score
    h_score = int(input("What is your homework score? "))
    if h_score < 0 or h_score > 25: # Check for validity of score
        print("Invalid score")
    else:
        valid_score = True

valid_score = False
while valid_score == False:
# User input assessment score
    a_score = int(input("What is your assessment score? "))
    if a_score < 0 or a_score > 50: # Check for validity of score
        print("Invalid score")
    else:
        valid_score = True

valid_score = False
while valid_score == False:
# User input final exam score
    f_score = int(input("What is your final exam score? "))
    if f_score < 0 or f_score > 100: # Check for validity of score
        print("Invalid score")
    else:
        valid_score = True

# Call grade_calc function with user inputs as arguments
print(grade_calc(h_score, a_score, f_score))

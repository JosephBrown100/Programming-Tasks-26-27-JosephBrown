"""
TASK: 01 Grade Calculation

# Skills: Input, output, selection
Write a program that asks the user for a percentage grade and prints the corresponding letter grade:
- A: 80-100
- B: 60-79
- C: 40-59
- D: <40
Include a function def get_grade(score):

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass


def numcheck(score):
    wrong = True
    while wrong:
        if score < 0 or score > 100:
            print("invalid score, re-enter")
            score = float(input("enter valid score"))
        wrong = False


def get_grade(score):
    numcheck(score)
    if 80.00 <= score and score <= 100.00:
        grade = "A"
        print(grade)
    elif 60 <= score and score < 80:
        grade = "B"
        print(grade)
    elif 40 <= score and score < 60:
        grade = "C"
        print(grade)
    else:
        grade = "D"
        print(grade)

if __name__ == "__main__":
    main()
    for i in range(0,10):
        score = float(input("please enter the students score: "))
        get_grade(score)

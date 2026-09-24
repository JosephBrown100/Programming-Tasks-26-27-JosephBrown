"""
TASK: 02 Times Tables

# Skills: Loops,input validation
Ask the user for a number, print the multiplication from 1 to 12 in a readable format:

Extend by using a function you can call for easy entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass

def timesT(Base,stval,enval):
    for i in range(stval,enval+1):
        mult = Base * i
        print("the value of", Base, "X", i, "=", mult)

def changeval(stval,enval):
    running = True
    while running:
        answer = input("do you want to change the starting and endinf mult? enter Y or N: ")
        if answer.upper() == "Y":
            change = True
            while change:
                print("what do you want to change the values to")
                try:
                    stval = int(input("what do you want the starting value to be: "))
                except:
                    print("error, enter a valid integer only")
                    continue
                try:
                    enval = int(input("what do you want the end val to be: "))
                except:
                    print("error, enter a valid integer only")
                    continue
                change = False
                running = False
                return stval, enval
        elif answer.upper() == "N":
            print("OK")
            running = False
        else:
            print("invalid answer, Re-enter")






if __name__ == "__main__":
    main()
    stval = 1
    enval = 12
    decision = True
    while decision:
        try:
            base = int(input("what times table do you want to see"))
            decision = False
        except:
            print("invalid, Re-enter")
    stval, enval = changeval(stval,enval)
    timesT(base,stval,enval)
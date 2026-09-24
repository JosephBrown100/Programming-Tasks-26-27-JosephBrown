"""
TASK: 06 Simple Login

# Skills: Selection, string comparison
Start with a correct username/password (extend if saved in a text file separately):
- Ask for login
- Print "Welcome" or "Access Denied {number} attempts remaining"
Only allow 3 attempts and close the file

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass

def getnamepass():
    actname = ""
    actpass = ""
    with open("Week_02_GCSE_Basics\\06_namepass.txt","r") as file:
        string = file.readline()
        strings = string.split(",")
        actname = strings[0]
        actpass = strings[1]
        return actname, actpass


def login(actname, actpass):
    tries = 0
    while tries < 3:
        print("please enter your username and password")
        name = input("enter your username: ")
        passw = input("enter your password: ")
        if name != actname or passw != actpass:
            print("access denied",2 - tries,"attempts remaining")
            tries += 1
        else:
            print("Welcome")
            return



if __name__ == "__main__":
    main()
actname, actpass = getnamepass()
login(actname,actpass)
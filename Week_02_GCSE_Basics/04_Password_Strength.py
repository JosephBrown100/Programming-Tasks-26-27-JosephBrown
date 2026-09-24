"""
TASK: 04 Password Strength

# Skills: Strings, loops, selection
Ask the user to enter a password, and check that they meet these conditions:
- At least 8 characters
- Contains a number
- Contains a captial and lower cased letter
- Extend for one special character
Print a response of weak, medium or strong for how many they pass.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def securepassword(password):
    n = 4
    digcount = 0
    upcount = 0
    locount = 0
    spcount = 0
    length = 0
    for char in password:
        if char.isdigit():
            digcount += 1
        if char.isupper():
            upcount += 1
        if char.islower():
            locount += 1
        if not(char.isalnum()):
            spcount += 1
        length += 1
    if digcount < 1:
        n -= 1
    if upcount < 1:
        n -= 1
    if locount < 1:
        n -= 1
    if spcount < 1:
        n -= 1
    if n == 4:
        print("strong")
    if n == 3:
        print("medium")
    if n <= 2:
        print("weak")


def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass


if __name__ == "__main__":
    password = input("enter a password")
    main()
    securepassword(password)
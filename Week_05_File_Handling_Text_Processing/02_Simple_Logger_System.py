"""
TASK: 02 Simple Logger System

# Create a script that appends time-stamped log entries to a file.
Menu:
- Add Log
- View Log
- Clear Log

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import datetime

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass

def add_log(filename):
    log = input("enter the log:\n")
    time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
    log = log + " : " + time
    with open(filename, "a") as file:
        file.write(log + "\n")
    return

def read_log(filename):
    with open(filename, "r") as text:
        file = text.read()
        print(file)
    return

def clear_log(filename):
    with open(filename, "w") as text:
        text = text.write("")
    clear = print("Cleared")
    return clear    



if __name__ == "__main__":
    main()
    filename = "Programming-Tasks-26-27-JosephBrown\\Week_05_File_Handling_Text_Processing\\one.txt"
    running = True    
    while running:    
        choice = input("do you want to 1: add a log, 2: read the log, or 3: clear the log:\n")
        if choice == "1":
            add_log(filename)
        elif choice == "2":
            read_log(filename)
        elif choice == "3":
            clear_log(filename)  
        
           
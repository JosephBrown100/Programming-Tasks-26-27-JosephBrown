"""
TASK: 01 2D Grid Manipulator

# Create an NxM grid resolver - https://bk2coady.medium.com/daily-coding-problem-62-bfe0e398247b
- Initialises a grid filled with zeros
- Allows user to "paint" coordinates
- Displays updated grid each time

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass


def gettablesize():
    running = True
    while running:
        try:
            rows = int(input("How many rows.\n"))
            columns = int(input("How many columns.\n"))
            running = False
        except:
            print("invalid. Retry.\n")
    return rows, columns 

def getcoordinate():
    running = True
    while running:
        try:
            rows = int(input("Which rows.\n"))
            columns = int(input("which columns.\n"))
            running = False
        except:
            print("invalid. Retry.\n")
    return rows, columns 

def array(rows, columns):
    Data = [["0"]*columns]*rows
    for i in Data:
        print(i)
    return Data

def getnewval():
    running = True
    while running:
        try:
            val = int(input("Enter the value you want to change the coordinate to.\n"))
            running = False
        except:
            print("invalid. Retry.\n")
    return val

def change_coordinate(Data):
    row, column = getcoordinate()
    Data[row-1][column-1] = getnewval()
    for i in Data:
        print(i)
    return Data


if __name__ == "__main__":
    main()
    forever = True
    while forever:
        choice = input("do you want to 1: Reset/create new table, or 2: Change a value:\n")
        if choice == "1":
            row,column = gettablesize()
            data = array(row,column)
        elif choice == "2":
            data = change_coordinate(data)
            
"""
TASK: 03 2D Array Adder

# 2D Array Added
Create a 2D arraw and allow user to:
- Append new values in
- read all current values
- delete a chosen entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass


def array(rows, columns):
    Data = [["0"]*columns]*rows
    for i in Data:
        print(i)
    return Data

def append_row(data):
    length =len(data[len(data)-1])
    newrow = ["0"]*length
    data.append(newrow)
    for i in data:
        print(i)
    return data


def append_column(data):
    data[0].append("0")
    for i in data:
            print(i)
    return data

def add_to_array(data):
    row = int(input("which row: "))
    column = int(input("which column: "))
    newdata = input("what do you want to replace it with: ")
    data[row-1][column-1] = newdata
    for i in data:
            print(i)
    return data

def Turn_val_null(data):
    row = int(input("which row: "))
    column = int(input("which column: "))
    nullval = "-"
    data[row-1][column-1] = nullval
    for i in data:
            print(i)
    return data

if __name__ == "__main__":
    rows = int(input("rows: "))
    columns = int(input("columns: "))
    data = array(rows, columns)
    running = True
    while running:
        choice = input("1,2,3,4 to append a row, append a column, add a peice of data to the array, remove a peice of data from the array respectively: ")
        try:
            if choice == "1":
                data = append_row(data)
            elif choice == "2":
                data = append_column(data)
            elif choice == "3":
                data = add_to_array(data)
            elif choice == "4":
                data = Turn_val_null(data)
        except:
            print("invalid re-enter")
"""
TASK: 01 Csv Writer

# Skills: CSV writing
CAsk the user for:
- Name
- age
- favourite colour
- anything you want
Append this to a CSV file (Extend: allow user to choose to edit the file and read the file)

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import csv

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass


def get_info():
    Name = input("What is your name: ")
    age = input("how old are you: ")
    colour = input("what is your favourite colour: ")
    food = input("What is your favourite food: ")
    return Name, age, colour, food


def add_to_csv(name, age, colour, food):
    with open("CSW_writer.csv","a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, colour, food])
        


def read_csv():
    with open("CSW_writer.csv","r") as file:
        reading = csv.reader(file)
        for row in reading:
            print(row)




if __name__ == "__main__":
    main()
    running = True
    while running:
        choice = input(("Do you want to append to the file, read the file, or exit. 1 to append, 2 to read, return to exit out: "))
        try:
            if choice == "1":
                name, age, colour, food = get_info()
                add_to_csv(name, age, colour, food)
            elif choice == "2":
                read_csv()
            elif len(choice) < 1:
                running = False
        except:
            print("Invalid answer, re-enter")
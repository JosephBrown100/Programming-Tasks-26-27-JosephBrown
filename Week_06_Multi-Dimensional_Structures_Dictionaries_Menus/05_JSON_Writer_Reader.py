"""
TASK: 05 Json Writer Reader

# Do some research into JSON
Prompt user for:
- Name
- Price
- Quantity
Store items into a JSON file with proper formatting
Then allow the user to open and convert to list of dictionaries and output the summary with averages.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import json

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass

def newitem():
    name = input("whats the name\n")
    price = float(input("whats the price\n"))
    amount = int(input("whats the amount\n"))
    
    new_item = {
        "name" : name,
        "price" : price,
        "quantity" : amount
    }

    with open("Programming-Tasks-26-27-JosephBrown\\Week_06_Multi-Dimensional_Structures_Dictionaries_Menus\\file.json", 'a') as file:
        json.dump(new_item, file)

def printfile():
    with open("Programming-Tasks-26-27-JosephBrown\\Week_06_Multi-Dimensional_Structures_Dictionaries_Menus\\file.json", "r") as file:
        contents = json.load(file)
        print(contents)



if __name__ == "__main__":
    main()
running = True
while running:
  choice = input("1,2, to add a new item, to print the file, respectively:\n ")
  if choice == "1":
    newitem()
  elif choice == "2":
    printfile()

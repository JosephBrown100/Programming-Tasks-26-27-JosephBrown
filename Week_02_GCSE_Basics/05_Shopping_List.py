"""
TASK: 05 Shopping List

# Skills: Loops, lists
Allow the user to add itemds to a shopping list until they type DONE
When they type DONE, print the list and ask if they want to edit any item.
They should select an item by number and allow them to ammend the item.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass

def shoppinglist():
    writing = True
    list = []
    while writing:
        item = input("Enter item to add to list, hit return when finished: ")
        if len(item) > 0:
            list.append(item)
        else:
            writing = False
    print(list)
    return list


def edit(list):
    editing = True
    while editing:
        answer = input("do you want to edit your list, enter Y/y or N/n: ")
        try:
            if answer == "Y" or "y":
                changing = True
                while changing:
                    Itemchange = input("Which item do you want to change, (press return to stop changing):")
                    if len(Itemchange) > 0:
                        for i in list:
                            if i == Itemchange:
                                replace = input("what do you want to replace it with: ")
                                del i
                                list.append(replace)
                    else:
                        changing = False
            editing = False
        except:
            if answer == "N" or "n":
                print("Okay")
            editing = False
    print(list)
    return(list)




if __name__ == "__main__":
    main()
    List = shoppinglist()
    edit(List)
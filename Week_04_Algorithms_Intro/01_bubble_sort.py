"""
TASK: 01 Bubble Sort

# Bubble Sort
Implement Bubble Sort on any size list:
- Do not use built-in sort()
- Count swaps
- Extend by

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass

def get_data():
    adding = True
    Data = []
    while adding:
        value = (input("enter your value or press enter to stop:\n"))
        if len(value) < 1:
            adding = False
        else:
            try:
                Data.append(float(value))
            except:
                print("Invalid, re-enter\n")
    return Data


def bubble_sort(data):
    length = len(data)
    for passes in range(length -1):
        for value in range(length - passes - 1):
            if data[value] > data[value + 1]:
                data[value],data[value + 1] = data[value + 1],data[value]
    return data 

if __name__ == "__main__":
    main()
    data = get_data()
    print("The base list is: ",data)
    sorted_list = bubble_sort(data)
    print("The orted list is: ",sorted_list)
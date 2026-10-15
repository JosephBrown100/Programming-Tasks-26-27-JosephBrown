"""
TASK: 02 Binary Search Tester

# Binary Search Tester
Generate a sorted list. Implement:
- iterative binary search
- recursive binary search
Then benchmark them with random inputs.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import random

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass


def random_array():
    data = []
    ranges = random.randint(2,2000)
    for i in range(ranges):
        value = random.randint(1,20)
        data.append(value)
    return data

def get_data_array():
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



def iterative_binary_search(data,target):
    low, high =  0, len(data)-1
    try:
        while low <= high:
            med = low + (high-low)//2
            if data[med] == target:
                return med
            elif data[med] < target:
                low = med + 1
            else:
                high = med - 1
    except:
        print("Target value is not in the list")

def recursive_binary_search(data,target,low,high):
    med = low + (high-low)//2
    if data[med] == target:
        return med
    if low > high:
        print("value not in list")
        return
    elif data[med] > target:
        return recursive_binary_search(data,target,low,med-1)
    else:
        return recursive_binary_search(data,target,med+1,high)
    




    
if __name__ == "__main__":
    main()
    choice = True
    while choice:
        array_type = input("Do you want to input a list or have one generated? 1 to input, 2 to generate\n")
        if array_type != "1" and array_type != "2":
            print("invalid, restart")
            continue
        search_type = input("Do you want to use an iterative binary search or a recursive one? 1 for iterative, 2 for recursive\n")
        if search_type != "1" and search_type != "2":
            print("invalid, restart")
            continue
        choice = False
    choice = True
    while choice:
        target = input("What value do you want to find?\n")
        try:
            target = float(target)
            if array_type == "1":
                data = get_data_array()
                data = bubble_sort(data)
                if search_type == "1":
                    index = iterative_binary_search(data,target) + 1
                    print("the index of your value is:",index)
                elif search_type == "2":
                    low = 0
                    high = len(data) - 1
                    index = recursive_binary_search(data,target,low,high) + 1
                    print("the index of your value is:",index)
            elif array_type == "2":
                data = random_array()
                data = bubble_sort(data)
                if search_type == "1":
                    index = iterative_binary_search(data,target) + 1
                    print("the index of your value is:",index)
                elif search_type == "2":
                    low = 0
                    high = len(data) - 1
                    index = recursive_binary_search(data,target,low,high) + 1
                    print("the index of your value is:",index)
        except:
            print("invalid target, re-enter")
        




    
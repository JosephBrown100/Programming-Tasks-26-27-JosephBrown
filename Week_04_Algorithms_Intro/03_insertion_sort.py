"""
TASK: 03 Insertion Sort

# Insertion Sort Tester
Generate an unsorted list (maybe use RNG). Implement:
- Insertion sort without using inbuild sorts
- Count number of comparions
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
    ranges = random.randint(2,200)
    for i in range(ranges):
        value = random.randint(1,200)
        data.append(value)
    return data

def Insertion_sort(data):
    length = len(data)
    for index in range(length):
        val = data[index]
        point = index
        while point > 0 and data[point-1] > val:
            data[point] = data[point-1]
            point -= 1
        data[point] = val
    return data


if __name__ == "__main__":
    main()
    data = random_array()
    print(data)
    data = Insertion_sort(data)
    print(data)
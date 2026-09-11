"""
TASK: 04 Linear Search

# Linear Search
Implement a linear search algorithm:
- Ask the user for a target value.
- Search a generated random list.
- Return the index or -1.
- Include `linear_search(values, target)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import random

def main():
    nothing = 0

def list_generator(values):
    Num_vals = random.randint(10,40)
    for i in range(0,Num_vals):
        Num = random.randint(1,50)
        values.append(Num)
    return values

def linear_search(values,target):
    found = True
    if target not in values:
        print(-1)
        return
    for i in values:
        if i == target:
            print(values.index(i))
            break




if __name__ == "__main__":
    main()
    target = int(input("what is the target value"))
    values = []
    list_generator(values)
    linear_search(values,target)
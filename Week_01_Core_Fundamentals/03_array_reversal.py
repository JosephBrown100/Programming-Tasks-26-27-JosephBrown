"""
TASK: 03 Array Reversal

# Array Reversal
Create a program that:
- Generates a list of random integers.
- Reverses the list manually (no slicing or .reverse).
- Includes a function `reverse_list(values)` that returns a new reversed list.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import random

def main():
    nothing = 0


def rand_list(values):
     Num_vals = random.randint(1,20)
     for i in range(0,Num_vals):
        Num = random.randint(1,100)
        values.append(Num)
     return values


def Reverse_list(values):
     Rev_Values = []
     for i in range(len(values) -1, -1, -1):
        Rev_Values.append(values[i])
     return Rev_Values



if __name__ == "__main__":
    values = []
    print(rand_list(values))
    print(Reverse_list(values))
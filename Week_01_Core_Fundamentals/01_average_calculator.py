"""
TASK: 01 Average Calculator

# Average Calculator
Write a Python program that:
- Prompts the user for a list of numbers.
- Stores them in a 1D list.
- Calculates the mean *without using built-in statistics libraries*.
- Includes input validation.
- Implements a reusable function: `calculate_average(values)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""


values = []

def main():
    b = True
    while b:
        num = input("How many numbers are there to average? ")
        if not num.isnumeric():
            print("Make sure to only enter integers")
            continue
        if int(num) <= 0:
            print("Make sure integer is greater than 0")
            continue
        else:
            num = int(num)
            b = False
    for i in range(num):
        val = float(input("Enter a number: "))
        values.append(val)


def calculate_average(values):
    n = 0
    for i in values:
        n += i
    return n / len(values)




if __name__ == "__main__":
    main()
    print(calculate_average(values))

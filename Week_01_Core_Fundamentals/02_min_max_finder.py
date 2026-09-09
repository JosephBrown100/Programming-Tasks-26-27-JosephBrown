"""
TASK: 02 Min Max Finder

# Min/Max Finder
Write a program that:
- Accepts a list of integers.
- Manually finds the min and max (no built-in min/max).
- Includes a function `find_min_max(values)` returning `(min_value, max_value)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    nothing = 0
    #nothing

def get_vals(values):
     loop = True
     while loop:
        num = input()
        if not num.isnumeric():
            print("Make sure to only enter integers")
            continue
        else:
            num = int(num)
            loop = False
        for i in range(num):
            val = float(input("Enter a number: "))
            values.append(val)

def find_min_max(values):
     min = values[0]
     max = values[0]
     for i in values:
        if i < min:
            min = i
     for i in values:
        if i > max:
            max = i
     return min, max


if __name__ == "__main__":
    values = []
    get_vals(values)
    print(find_min_max(values))


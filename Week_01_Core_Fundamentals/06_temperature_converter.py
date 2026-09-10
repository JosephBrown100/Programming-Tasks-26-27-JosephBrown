"""
TASK: 06 Temperature Converter

# Temperature Converter
Build a converter tool:
- Convert Celsius <-> Fahrenheit.
- Provide a looped menu.
- Validate user input.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    pass


def convert_CF():
    celc = float(input("how many degrees c "))
    faren = (celc * (9/5)) + 32
    return faren


def convert_FC():
    faren = float(input("how many faren heights "))
    celc = (faren - 32) * (5/9)
    return celc


if __name__ == "__main__":
    main()
    while True:
        cf = input("Do you want to convert C to F or F to C. Enter 'C to F' or 'F to C' depending on want: ")
        while cf not in ("C to F","F to C"):
            print("please make sure your answer is valid")
            cf = input("Do you want to convert C to F or F to C. Enter 'C to F' or 'F to C' depending on want: ")
            continue
        if cf == "C to F":
            print(convert_CF())
        if cf == "F to C":
            print(convert_FC())



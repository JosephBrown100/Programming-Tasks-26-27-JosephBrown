"""
TASK: 05 String Parser

# String Parser
Write a parser that:
- Accepts a sentence from the user.
- Splits it into words manually (not using split()).
- Outputs number of words + list of words.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    n = 0

def parser(string):
    split = []
    temp = []
    for char in string:
        if char == " ":
            if temp:
                split.append("".join(temp))
                temp = []
                continue
        else:
            temp.append(char)
    if temp:
        split.append("".join(temp))
    print(split)



if __name__ == "__main__":
    main()
    string = input()
    parser(string)

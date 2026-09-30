"""
TASK: 05 File Word Search

# Skills: File reading, loops, Data mining
Ask user for a filename and a search term. https://sherlock-holm.es/ascii/ is a site that has the entire collection of Sherlock Holmes
Load the file and count how many lines contain the search term

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass

def line_count(term,name):
    count = 0
    with open("Programming-Tasks-26-27-JosephBrown\\Week_03_Arrays_Lists_CSV_Basics\\"+name, "r") as file:
        for line in file:
            if term in line:
                count += 1
    return count



if __name__ == "__main__":
    main()
    term = input("What word are you looking for: ")
    name = input("what is the file name: ")
    times = line_count(term,name)
    print(times)

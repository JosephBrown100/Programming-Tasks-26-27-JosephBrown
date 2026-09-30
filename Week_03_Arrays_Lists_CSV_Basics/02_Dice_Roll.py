"""
TASK: 02 Dice Roll

# Skills: RNG, Loops
Simulate rolling a six-sided die X number of times:
Print each roll, store all values in a list of updated totals for each number (56 ones for example):
Allow the user to print:
- Totals for each side
- average dice roll
- Counts for each of the 6 sides
- Extend (look up how to use mathplotlib and produce a bar graph for all of the statistics)

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import random


def main():
    pass

def dice(times, rolls):
    average = 0
    for i in range(times):
        roll = random.randint(1,6)
        print(roll)
        rolls[roll - 1] += 1
        average += roll
    return rolls, (average/times)







if __name__ == "__main__":
    main()
    rolls = [0, 0, 0, 0, 0, 0]
    times = input("how many times do you want to roll the die: ")
    casting = True
    while casting:
        try:
            times = int(times)
            casting = False
        except:
            times = input("invalid input, re-enter: ")
    rolls, average = dice(times,rolls)
    deciding = True
    while deciding:
        choice = input("Totals, average, counts or return to exit: ")
        try:
            if choice == "Totals":
                print(rolls)
            elif choice == "average":
                print(average)
            elif choice == "counts":
                n = 1
                for face, count in enumerate(rolls, 0):
                    face += 1
                    count = count * n
                    print(face,":",count)
                    n += 1
            elif len(choice) < 1:
                deciding = False
        except:
            print("invalid")

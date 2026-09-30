"""
TASK: 04 Temp Stats Csv

# Skills CSV read, simple maths
Go to this site https://www.metoffice.gov.uk/hadobs/hadcet/data/download.html and download the txt file
Daily Mean Temperature.
This file has dates and daily temperatures:
- Read all of the values
- Find the highest, lowest and average
- Print those three values
Extend - See how you can potentially use the dates to chart daily temp changes by years, by months
by day comparisons over time. Maybe chart them using mathplotlib or another library. Just see what you can do with it

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass

def minmax():
    max = 0
    min = 10000
    total = 0
    n = 0
    with open("Programming-Tasks-26-27-JosephBrown\\Week_03_Arrays_Lists_CSV_Basics\\meantemp_daily_totals.txt","r") as file:
        for i in file:
            vals = i.split(" ")
            temp = vals[-1]
            temp = float(temp)
            if temp > max:
                max = temp
            if temp < min:
                min = temp
            total += temp 
            n += 1
        return max, min, (total/n)


if __name__ == "__main__":
    main()
    x, y, z = minmax()
    print("maximum is:", x, "minimum is:", y, "average is:", z)
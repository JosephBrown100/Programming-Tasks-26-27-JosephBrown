"""
TASK: 04 Student Grades Table

# Use a dictionary of lists e.g
grades = {
  "Alice": [80, 85, 90],
  "Ben": [70, 60, 75]
}
Add:
- Function to compute class averages
- Function to add student
- Function to remove student

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass

grades = {
  "Alice": [80, 85, 90],
  "Ben": [70, 60, 75]
}

def grade_avg(grades, student):
  avg = sum(grades[student]) / len(grades[student])
  return avg

def grade_avg_all(grades):
  total = 0
  total_length = 0
  for i in grades:
    total = sum(grades[i]) + total
    total_length = len(grades[i]) + total_length
  avg = total / total_length
  return avg

def add(grades):
  marks = []
  name = input("What is the students name.\n")
  gnum = int(input("how many mark numbers.\n"))
  for i in range(gnum):
    mark = int(input("how many marks,\n"))
    marks.append(mark)
  grades[name] = marks
  return grades

     


if __name__ == "__main__":
    main()
running = True
while running:
  choice = input("1,2,3 to add student,calculate a students average, calculate the class average, respectively:\n ")
  if choice == "1":
    add(grades)
  elif choice == "2":
    student = input("What is their name.\n")
    avg = grade_avg(grades,student)
    print(student, avg)
  elif choice == "3":
    avg = grade_avg_all(grades)
    print("class:",avg)

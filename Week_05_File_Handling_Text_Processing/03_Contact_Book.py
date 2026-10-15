"""
TASK: 03 Contact Book

# Store contacts in a text file, each line containing
name,phone,email
Program must allow:
- Add contact
- Search contact (sequential search)
- Display all

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass

def addcontact(filename):
    name, phone, email = input("please enter the name:\n"), input("please enter the phone number:\n"), input("please enter the email address:\n")
    with open(filename, "a") as file:
        file = file.write(name + "," + phone + "," + email + "\n")

def searchcontact(filename):
    wantedcontact = input("what is the name/phone-number/email of the person you are looking for:\n")
    found = False
    with open(filename, "r") as file:
        for line in file:
            info = line.split(",")
            if info[0] == wantedcontact:
                print("Name:",info[0],"  Phone-number:",info[1],"  Email:",info[2].strip("\n"))
                found = True
            elif info[1] == wantedcontact:
                print("Name:",info[0],"  Phone-number:",info[1],"  Email:",info[2].strip("\n"))
                found = True
            elif info[2].strip("\n") == wantedcontact:
                print("Name:",info[0],"  Phone-number:",info[1],"  Email:",info[2].strip("\n"))
                found = True
        if found == False:
            print("person is not in your contacts")

def show_all(filename):
    list = []
    with open(filename, "r") as file:
        for line in file:
            info = line.split(",")
            list.append("Name: " + info[0] + "  Phone-number: " + info[1] + "  Email: " + info[2].strip("\n") + "\n")
        return list

def options():
    filename = "Programming-Tasks-26-27-JosephBrown\\Week_05_File_Handling_Text_Processing\\Contacts.txt"
    choose = input("Do you want to 1: add a new contact, 2: search for a contact, or 3: view all contacts?\n")
    if choose == "1":
        addcontact(filename)
    elif choose == "2":
        searchcontact(filename)
    elif choose == "3":
        all = show_all(filename)
        for i in all:
            print(i)
    else:
        print("error, Restart")


if __name__ == "__main__":
    main()
    running = True
    while running:
        options()
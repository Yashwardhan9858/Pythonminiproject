def addNumber(contacts):
    y=True
    while (y):
        person=input("Enter the name of the person: ")
        number=input("Enter the number: ")
        if (len(number)!=10):
            print("Number is not of the right length")
            continue
        contacts[person]=number
        x=input("Do you wish to add another contact(Y/N): ")
        x=x.upper()
        if (x=="Y"):
            y=True
        elif (x=="N"):
            y=False
        else:
            print("Invalid input")
            break
def updateNumber(contacts):
    y=True
    while (y):
        person=input("Enter the name of the person's contact you want to edit: ")
        contacts[person]=input("Enter the number: ")
        x=input("Do you wish to edit more(Y/N): ")
        x=x.upper()
        if (x=="Y"):
            y=True
        elif (x=="N"):
            y=False
        else:
            print("Invalid input")
            break

def deleteNumber(contacts):
    y=True
    while (y):
        deleter=input("Whose contact do ypu wish to delete: ")
        del contacts[deleter]
        x=input("Do you wish to delete more(Y/N): ")
        x=x.upper()
        if (x=="Y"):
            y=True
        elif (x=="N"):
            y=False
        else:
            print("Invalid input")
            break

def searchNumber(contacts):
    y=True
    while (y):
        search=input("Whose number do you want to search: ")
        print(contacts[search])
        x=input("Do you wish to search more(Y/N): ")
        if (x=="Y"):
            y=True
        elif (x=="N"):
            y=False
        else:
            print("Invalid input")
            break
contacts={}
print("Welcome to Contactbook")
z=True
while (z):
    print("Actions you can perform in the contactbook: ")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6.Exit")
    x=int(input("Enter your choice(1/2/3/4/5/6): "))
    if (x==1):
        addNumber(contacts)
    elif (x==3):
        updateNumber(contacts)
    elif (x==5):
        print("Your contacts are : ",contacts)
    elif (x==4):
        deleteNumber(contacts)
    elif (x==2):
        searchNumber(contacts)
    elif (x==6):
        break
    else:
        print("Did not enter a valid operation")
        break
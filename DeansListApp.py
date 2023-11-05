#Name: Tejas Shastri
#Title: Dean's List App
#Description: This app determines if a student is part of the Dean's List or Honor Roll


last_name = input("Please enter a student's last name, or \"ZZZ\" to quit. ")
while (last_name != "ZZZ"):             #While loop checks for exit string
    first_name = input("Please enter the student's first name. ")
    GPA = float(input("Please enter the student's GPA: "))
    if(GPA>=3.5):
        print(first_name + " " + last_name + " has made the Dean's List. ")
    elif(3.5>GPA>=3.25):
        print(first_name + " " + last_name + " has made the Honor Roll. ")
    else: print("Student has not made Dean's List or Honor Roll. ")
    last_name = input("Please enter a student's last name, or \"ZZZ\" to quit. ") #Updating last_name

print("Goodbye!")  
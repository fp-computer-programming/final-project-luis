# author: LM (AMDG) 5/3/22
# file manager for student hours

# Asks user for their students' info and then puts it into a txt file
def student_info():
    name = input("Please enter the student's name: ")
    address = input("Please enter the student's address: ")
    phone = input("Please enter Parent's phone number: ")
    hours = float(input("Please enter the student's number of hours completed: "))
    with open('students_service_hours.txt', 'a') as infile:
        infile.write('Name: {0}'.format(name))
        infile.write('\n')
        infile.write('Address: {0}'.format(address))
        infile.write('\n')
        infile.write("Parent's Phone Number: {0}".format(phone))
        infile.write("\n")
        infile.write("Student's hours: {0}".format(hours))
        infile.write("\n")
        infile.write("\n")
    return name, address, phone, hours

# asks user if hey are  goint to add another person
def repeat_student_info():
    while True:
        anotherstudent = input("Will you be adding another student? Enter 'Y' if yes or 'N' if no: ").capitalize()
        if anotherstudent == 'Y':
            print("You will be adding another student...")
            student_info()
        elif anotherstudent == 'N':
            print("Thank you. Have a good day.")
            break
        elif anotherstudent != 'Y' or 'N':
            print("Enter a 'Y' or 'N'")
            continue
        return anotherstudent
while True:
    repeat_student_info()
    if repeat_student_info() == 'N':
        break




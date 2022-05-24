# author: LM (AMDG) 5/3/22
# This is the dictionary where students will be the keys and their hours will be values
dictionary = {}
# This dictionary is for the students who are under the required minimum of hours
new_dict = {}
# this is the list of the inputs the user will make for the students name
keys = []
# this list is the number of hours the student has
values = []
# file manager for student hours
# Asks user for their students' info and then puts it into a txt file
def student_info():
    global values
    global dictionary
    global keys
    name = input("Please enter the student's name: ")
    keys.append(name)
    address = input("Please enter the student's address: ")
    phone = input("Please enter Parent's phone number: ")
    hours = float(input("Please enter the student's number of hours completed: "))
    values.append(hours)
    # temporary dictionary made
    newdictionary = {name: hours}
    dictionary.update(newdictionary)
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
    return
    
def new_dictionary():
    global new_dict
    global keys
    global values
    # using enumerate to go throught the lists and usinf the indexes to append to the 'new_dict'
    for index, value in enumerate(keys and values):
        if value < 20:
            new_dict.update({keys[index]: values[index]})
            del keys[index] 
            del values[index]
    return


# asks user if hey are  goint to add another person
def repeat_student_info():
    while True:
        anotherstudent = input("Will you be adding another student? Enter 'Y' if yes or 'N' if no: ").capitalize()
        if anotherstudent == 'Y':
            print("You will be adding another student...")
            student_info()
            new_dictionary()
        elif anotherstudent == 'N':
            break
        elif anotherstudent != 'Y' or 'N':
            print("Enter a 'Y' or 'N'")
            continue
        return anotherstudent

while True:
    repeat_student_info()
    if repeat_student_info() == 'N':
        break
    elif repeat_student_info() == 'Y':
        continue
    break
if new_dict == {}:
        print("All students have completed their hours!!!")
else:
    new_question = input("Do you want to see the names of students who have not completed their hours and their hours? Enter Y for yes or N if no: ").capitalize()
    if new_question == "Y":
        print(new_dict)
    else:
        print("Have a good rest of the day")
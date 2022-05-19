#adds students to dictionary
# This is the dictionary where students will be the keys and their hours will be values
dictionary = {}
# This dictionary is for the students who are under the required minimum of hours
new_dict = {}
# this is the list of the inputs the user will make for the students name
keys = []
# this list is the number of hours the student has
values = []
while True: 
    new_person = input("Will you be adding more people? If yes enter y if no enter n: ").capitalize()
    if new_person == 'Y':
        def dictionary_student():
            global dictionary
            global keys
            hours = int(input("How many hours have been completed? "))
            values.append(hours)
            name = input("Enter your name: ")
            keys.append(name)
            # here a temporary dictionary is made. used to update 'dictionary'
            newdictionary = {name: hours}
            dictionary.update(newdictionary)
            return
        dictionary_student()
        def new_dictionary():
            global new_person
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
        new_dictionary()
    else:
        break
if new_dict == {}:
    print("All students have completed their hours!!!")
else:
    new_question = input("Do you want to see the names of students and their hours? Enter Y for yes or N if no: ")
    if new_question == "y":
        print(new_dict)
    else:
        print("Have a good rest of the day")
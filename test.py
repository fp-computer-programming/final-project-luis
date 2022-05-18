#adds students to dictionary
dictionary = {}
keys = []
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
            newdictionary = {name: hours}
            dictionary.update(newdictionary)
            print(dictionary)
            return
        dictionary_student()
    else:
        break
get_values = dictionary.values()
def students_under_minimum():
    new_dictionary = {}
    global get_values
    global dictionary
    global values
    global keys
    for index, value in values:
        if value < 20:
            print(index)
            print(keys[index])
    return
students_under_minimum()
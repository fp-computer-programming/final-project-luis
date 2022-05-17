#adds students to dictionary
dictionary = {}
while True: 
    new_person = input("Will you be adding more people? If yes enter y if no enter n: ").capitalize()
    if new_person == 'Y':
        def dictionary_student():
            global dictionary
            hours = int(input("How many hours have been completed? "))
            name = input("Enter your name: ")
            newdictionary = {name: hours}
            dictionary.update(newdictionary)
            print(dictionary)
        dictionary_student()
    else:
        break
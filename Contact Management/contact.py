def add_person():
    name = input("Name: ")
    age = int(input("Age: "))
    email = input("Email: ")
    person = {"name": name, "age": age, "email": email}
    print("Person added successfully")
    return person

def delete_person(people, name):
    for i, person in enumerate(people):
        if person["name"] == name:
            del people[i]
            return True
    return False

def update_person(people, name):
    for i, person in enumerate(people):
        if person["name"] == name:
            person["age"] = int(input("New Age: "))
            person["email"] = input("New Email: ")
            return True
    return False

def display_people(people):
    for person in people:
        print(f"Name: {person['name']}, Age: {person['age']}, Email: {person['email']}")

def search_person(people, name):
    for person in people:
        if person["name"] == name:
            return person
    return None


print("Hi! and welcome to the contact management system \n")
while True:
        choice = input("You can 'Delete', 'Add', 'Update' or 'Q' for quit: ").lower()
        people = []
        if choice == 'add':
            person = add_person()
            people.append(person)
        elif choice == 'update':
            name = input("Enter the name of the person you want to update: ")
            if update_person(people, name):
                print("Person updated successfully!")
            else:
                print("Person not found!")
                continue
        elif choice == 'delete':
            name = input("Enter the name of the person you want to delete: ")
            if delete_person(people, name):
                print("Person deleted successfully!")
            else:
                print("Person not found!")
                continue
        elif choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
            
def add_person():
    id = input("Your Id: ")
    name = input("Name: ")
    age = int(input("Age: "))
    email = input("Email: ")
    person = {"Id": id, "name": name, "age": age, "email": email}
    print("Person added successfully")
    return person

def delete_person(people, id):
    for i, person in enumerate(people):
        if person["id"] == id:
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

def search_person(people, id):
    for person in people:
        if person["id"] == id:
            return person
    return None


print("Hi! and welcome to the contact management system \n")
people = []
while True:
        choice = input("You can 'Search', 'Delete', 'Add', 'Update' or 'Q' for quit: ").lower()
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
            if delete_person(people, id):
                print("Person deleted successfully!")
            else:
                print("Person not found!")
                continue
        elif choice =='search':
            id = input("Enter the id of the person you want to search: ")
            person = search_person(people, id)
            if person:
                print(f"Name: {person['name']}, Age: {person['age']}, Email: {person['email']}")
            else:
                print("Person not found!")
        elif choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
            
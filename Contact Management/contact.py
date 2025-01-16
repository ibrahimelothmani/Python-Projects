import json

def add_person():
    name = input("Name: ")
    age = int(input("Age: "))
    email = input("Email: ")
    person = {"name": name, "age": age, "email": email}
    print("Person added successfully!")
    return person

def delete_person(people, name):
    for i, person in enumerate(people):
        if person["name"] == name:
            del people[i]
            print("Person deleted successfully!")
            return True
    print("Person not found!")
    return False

def update_person(people, name):
    for person in people:
        if person["name"] == name:
            person["age"] = int(input("New Age: "))
            person["email"] = input("New Email: ")
            print("Person updated successfully!")
            return True
    print("Person not found!")
    return False

def display_people(people):
    if not people:
        print("No contacts available.")
    for person in people:
        print(f"Name: {person['name']}, Age: {person['age']}, Email: {person['email']}")

def search_person(people, name):
    for person in people:
        if person["name"] == name:
            print(f"Name: {person['name']}, Age: {person['age']}, Email: {person['email']}")
            return person
    print("Person not found!")
    return None

def main():
    print("Hi! Welcome to the contact management system \n")
    people = []

    try:
        with open("contacts.json", "r") as file:
            people = json.load(file)["contacts"]
    except FileNotFoundError:
        print("No previous contacts found, starting with an empty contact list.")

    while True:
        choice = input("You can 'Search', 'Delete', 'Add', 'Update', 'Display' or 'Q' for quit: ").lower()
        if choice == 'add':
            person = add_person()
            people.append(person)
        elif choice == 'update':
            name = input("Enter the name of the person you want to update: ")
            update_person(people, name)
        elif choice == 'delete':
            name = input("Enter the name of the person you want to delete: ")
            delete_person(people, name)
        elif choice == 'search':
            name = input("Enter the name of the person you want to search: ")
            search_person(people, name)
        elif choice == 'display':
            display_people(people)
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

    with open("contacts.json", "w") as file:
        json.dump({"contacts": people}, file)

if __name__ == "__main__":
    main()

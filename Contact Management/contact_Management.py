print("Welcome to the second Project")

people = []

for i in range(3):
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    email = input("Enter Email: ")
    person = {"name": name, "age": age}
    people.append(person)
    
print("List of People: \n", people)
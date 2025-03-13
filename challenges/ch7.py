
my_list = [100, 200, 300, 400, 500]

counter = 0

while(counter < len(my_list)):
    print(my_list[counter])
    counter += 1
    
print("\n second Solution \n")
 
for item in my_list:
    print(item)
    
print("\n third Solution \n")

for i in range(len(my_list)):
    print(my_list[i])
    

print("\n Fourth Solution \n")

new_list = [x for x in my_list]
print(new_list)

print("\n Fifth Solution using filter \n")

filtered_list = [x for x in my_list if x < 400]
print(filtered_list)
# output [100, 200, 300]
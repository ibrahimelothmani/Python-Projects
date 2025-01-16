operand = input("Enter Number : ")
operand2 = input("Enter Number : ")

sign = input("Sign : ")

if sign == '+':
    result = float(operand) + float(operand2)
    print(f"{operand} + {operand2} = {result}")

elif sign == '-':
    result = float(operand) - float(operand2)
    print(f"{operand} - {operand2} = {result}")

elif sign == '*':
    result = float(operand) * float(operand2)
    print(f"{operand} * {operand2} = {result}")

elif sign == '/':
    if float(operand2) == 0:
        print("Error: Division by zero")
    else:
        result = float(operand) / float(operand2)
        print(f"{operand} / {operand2} = {result}")
else:
    print("Error: Invalid sign")
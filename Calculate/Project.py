operand = input("Enter Number : ")
operand2 = input("Enter Number : ")
sign = input("Sign : ")

while(True):
    try:
        operand = float(operand)
        operand2 = float(operand2)
    except:
        print("Error: Invalid input. Please enter numbers.")
        exit()

    if sign == '+':
        result = operand + operand2
        print(f"{operand} + {operand2} = {result}")
        break
    elif sign == '-':
        result = operand - operand2
        print(f"{operand} - {operand2} = {result}")
        break
    elif sign == '*':
        result = operand * operand2
        print(f"{operand} * {operand2} = {result}")
        break
    elif sign == '/':
        if operand2 == 0:
            print("Error: Division by zero")
            break
        else:
            result = operand / operand2
            print(f"{operand} / {operand2} = {result}")
            break
    else:
        print("Error: Invalid sign")
        break
    

#if sign == '+':
#    result = operand + operand2
#    print(f"{operand} + {operand2} = {result}")
#
#elif sign == '-':
#    result = operand - operand2
#    print(f"{operand} - {operand2} = {result}")
#
#elif sign == '*':
#    result = operand * operand2
#    print(f"{operand} * {operand2} = {result}")
#
#elif sign == '/':
#    if operand2 == 0:
#        print("Error: Division by zero")
#    else:
#        result = operand / operand2
#        print(f"{operand} / {operand2} = {result}")
#else:
#    print("Error: Invalid sign")

for clac in range(1,10,5):
 opt = input("What operation do you wanna do +,-,/,* = ")

 number1 = float(input("Enter the first Number = "))
 number2 = float(input("Enter the second Number = "))
 
 if opt == "+":
    result = number1 + number2
    print(result)
 elif opt == "-":
    result = number1 - number2
    print(result)
 elif opt == "/":
    result = number1 / number2
    print(result)
 elif opt == "*":
    result = number1 * number2
    print(result)
 else:
    print("invalid input")
    result = None 
    
if result is not None:
    print("The Output is :", result )
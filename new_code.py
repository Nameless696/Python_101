def opt(operator, num1, num2):
 
    if operator == '+':
        result = num1 + num2
        
    elif operator == '-':
        result = num1 - num2
        
    elif operator == '*':
        result = num1 * num2
        
    elif operator == '/':
        result = num1 / num2
        
    else:
        print("Invalid operator.")
        return None

    return result

operator = input("Enter an operator (+, -, *, /): ") 
print()

number1 = float(input("Enter the first number: "))
print()

number2 = float(input("Enter the second number: "))
print()

result = opt(operator, number1, number2)

if result is not None:
    print("Result:", result)

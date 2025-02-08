# Corrected version of the calculator code
first = input("Enter 1st number: ")
second = input("Enter 2nd number: ")
operator = input("Enter any operator (+, -, *, /, %): ")

# Ensure the inputs are valid numbers
try:
    num1 = float(first)
    num2 = float(second)
except ValueError:
    print("Invalid input! Please enter numeric values.")
    exit()

if operator == '+':
    result = num1 + num2
    print("Sum = " + str(result))
elif operator == '-':
    result = num1 - num2
    print("Difference = " + str(result))
elif operator == '*':
    result = num1 * num2
    print("Product = " + str(result))
elif operator == '/':
    if num2 == 0:
        print("Can't divide by zero")
    else:
        result = num1 / num2
        print("Division = " + str(result))
elif operator == '%':
    if num2 == 0:
        print("Can't divide by zero")
    else:
        result = num1 % num2
        print("Modulus = " + str(result))
else:
    print("Invalid input!")

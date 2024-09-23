# Function to find the remainder of two numbers
def find_remainder(number1, number2):
    try:
        remainder = number1 % number2
        return remainder
    except ZeroDivisionError:
        return "Division by zero is not allowed."

# Taking input from the user
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Finding the remainder
result = find_remainder(number1, number2)

# Displaying the result
print(f"The remainder when {number1} is divided by {number2} is: {result}")

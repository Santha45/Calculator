import sys

# Function for addition
def add(x, y):
    return x + y

# Check if the correct number of arguments are passed
if len(sys.argv) != 3:
    print("Usage: python calc.py <num1> <num2>")
    sys.exit(1)

# Get the numbers from the command-line arguments
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

# Perform the addition
result = add(num1, num2)

# Print the result
print(f"{num1} + {num2} = {result}")

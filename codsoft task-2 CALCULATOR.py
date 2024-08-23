
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def product(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"

print("Welcome to the Calculator!")
print("Choose an operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("Enter your choice :1 / 2/ 3/ 4 ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", sub(num1, num2))
elif choice == '3':
    print("Result:", product(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid choice. Please select 1, 2, 3, or 4.(donot give any choice other than this )")

print("Thank you for using the Calculator!")





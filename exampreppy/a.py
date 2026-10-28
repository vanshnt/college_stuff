#A. Basic Python Programs


# 1. Accept two numbers and display their sum, difference, product and division.
def calc(a, b):
    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Product:", a * b)
    print("Division:", a / b)

calc(10, 5)
print("")

# 2. Accept a student's name and marks and display the average using an f-string.

def printt(name, mark1, mark2, mark3, mark4):
    print(f"{name}: Average: {(mark1+mark2+mark3+mark4)/4}")
printt("Vansh", 56, 54, 86, 79)


# 3. Swap two numbers.
print("")
def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    print(a, b)
swap(5, 6)


# 4. Convert user input into int and float and display their types

print("")
a = int(input("Enter num 1: "))
b = float(input("Enter num 2: "))

print("num 1 is ", type(a))
print("num 2 is ", type(b))


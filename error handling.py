
try:
    a = int(input("First number:"))
    b = int(input("Second number:"))
    print('Result:', a/b)
except ValueError:
    print("Please enter valid number")
except ZeroDivisionError:
    print("Cannot divide by zero.")

while True:
    try:
        age = int(input("Enter your age"))
        break     # leave the loop if conversion worked
    except ValueError:
        print(" Please enter a whole number.")
print("Age recorded:",age)

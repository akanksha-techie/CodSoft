print("Choose the operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number:"))
choice = input("Enter operation (1/2/3/4): ")
if choice == "1":
    result = num1 + num2
    op = "+"
elif choice == "2":
    result = num1 - num2
    op = "-"
elif choice == "3":
    result = num1 * num2
    op = "*"
elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        op = "/"
    else:
        result = "Error :Division by Zero"
        op = "/"
else:
    result = "Invalid choice"
    op = "?"
print(f"Result: {num1} {op} {num2} = {result}")
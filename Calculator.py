# Calculator
operators = ["+", "-", "*", "/", "**"]
new_op = "  ".join(operators)

print(new_op)
op = input("Select one of the above operations for simple calculations:  ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


if op == "+":
    print("The sum is", num1+num2)
elif op == "-":
    print("The difference is", num1-num2)
elif op == "*":
    print("The product is", num1*num2)
elif op == "/":
    print("The quotient is", num1/num2)
elif op == "**":
    print("The power:", num1**num2)

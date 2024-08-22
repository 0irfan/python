def calculator():
    oper_1 = int(input("Enter First Number: "))
    oper_2 = int(input("Enter Second Number: "))
    operator = input("Enter operator: ")
    if operator == "+":
        return oper_1 + oper_2
    elif operator == "-":
        return oper_1 - oper_2
    elif operator == "*":
        return oper_1 * oper_2
    elif operator == "//":
        return oper_1 // oper_2
    else:
        return "Invalid operator"
# Test the function
a = calculator()  # Output
print(a)  # Output
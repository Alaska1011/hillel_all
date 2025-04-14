while True:
    print("Enter firs number: ")
    num1 = float(input())
    print("Enter operation (+, -, *, /): ")
    operation = input()
    print("Enter second number: ")
    num2 = float(input())
    if operation == '+':
        result = num1 + num2
        print("result:", result)
    elif operation == '-':
        result = num1 - num2
        print("result:", result)
    elif operation == '*':
        result = num1 * num2
        print("result:", result)
    elif operation == '/':
        if num2 == 0:
            print("Error: divisor cannot be 0-supplemented!")
        else:
            result = num1 / num2
            print("result:", result)
    else:
        print("Error: Invalid operation! Try again.")

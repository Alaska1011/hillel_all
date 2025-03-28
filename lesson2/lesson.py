
number = int(input("Enter 4-digit number: "))

if 0<= number <=9999:
    thousands = number // 1000

    hundreds = (number // 100) % 10

    tens = (number // 10) % 10

    units = number % 10

    print(thousands)

    print(hundreds)

    print(tens)

    print(units)
else:
    print("давай по новой")
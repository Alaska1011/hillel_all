a = int(input('enter n number: '))

n = 0

while a>0:

    z = a % 10
    a = a // 10
    n = n*10
    n = n + z
else:
    print("переделывай")
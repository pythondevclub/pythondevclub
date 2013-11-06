number = int(input())

if number == 98 or number % 23 == 0 or (number % 24 == 6 and number < 1000):
    print('YES')       
else:
    print('NO')

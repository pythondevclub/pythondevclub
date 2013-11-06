x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

if (y1 - y2) * x3 + (x2 - x1) * y3 + (x1 * y2 - x2 * y1) == 0:
    print('YES')
else:
    print('NO')


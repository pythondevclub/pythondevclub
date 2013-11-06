x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 < 0 or x2 < 0 or y1 < 0 or y2 < 0 or (x1 == x2) or (y1 == y2):
    print('NO')
elif (x1 - x2 in [-2, 2]) and (y1 - y2 in [-1, 1]):
    print('YES')
elif (x1 - x2 in [-1, 1]) and (y1 - y2 in [-2, 2]):
    print('YES')
else:
    print('NO')


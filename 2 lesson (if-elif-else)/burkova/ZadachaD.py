number = int(input())

if number % 34 in [2, 3, 5, 7, 11, 13, 17, 19]:
    print('Case1')
elif number % 26 in [2, 3, 5, 7, 11, 13, 17, 19]:
    print('Case2')
else:
    print('Case3')

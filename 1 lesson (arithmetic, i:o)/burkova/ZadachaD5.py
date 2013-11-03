first_digit = int(input())
second_digit = int(input())

is_first_digit_max = (first_digit // second_digit + 2) // (first_digit // second_digit + 1) % 2
is_second_digit_max = (is_first_digit_max + 1) % 2

print(first_digit * is_first_digit_max + second_digit * is_second_digit_max)

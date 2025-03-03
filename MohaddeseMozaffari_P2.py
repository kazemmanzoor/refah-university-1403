def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def largest_two_digit_prime():
    for num in range(99, 9, -1):
        if is_prime(num):
            return num

print(largest_two_digit_prime())

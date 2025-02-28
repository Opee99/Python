# conditions for a prime number:
# has to be greater than 1.
# only factors are 1 and itself.

n = int(input("Enter your number: "))


def prime_number_check(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


prime_number_check(n)
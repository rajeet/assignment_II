# Write a function, is_prime, that takes an integer and returns True if
# # the number is prime and False if the number is not prime.


integer = int(input("Enter a number: "))
if integer > 1:
    for i in range(2, integer):
        if integer % i == 0:
            print(f"{integer} Not a prime number")
            break
    else:
        print(f"{integer} is a prime number")
else:
    print(f"{integer} number is not a prime number")
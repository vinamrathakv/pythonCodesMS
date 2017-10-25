# count the number of primes below 10000

# Check whether number is prime 
def isPrime(number):
    for divisor in range(2, number // 2 + 1):
        if number % divisor == 0: # If true, number is not prime
            return False # number is not a prime

    return True # number is prime

def main():
    count = 0
    N = 10000
    for number in range(2, N):
        if isPrime(number):
            #print(number)
            count += 1

    print("The number of prime numbers less than", 10000, "is", count)


main()

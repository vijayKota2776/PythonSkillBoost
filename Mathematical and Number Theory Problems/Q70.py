def sieve_of_eratosthenes():
    try:
        n = int(input("Enter upper limit to find prime numbers: "))
        
        if n < 2:
            print("There are no prime numbers less than 2!")
            return
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        steps = []
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                marked = []
                for j in range(i * i, n + 1, i):
                        is_prime[j] = False
        primes = [num for num, is_p in enumerate(is_prime) if is_p]
        print(f"\nPrime numbers up to {n}:")
        print(primes)
        print(f"\nTotal prime numbers found: {len(primes)}")
        if steps:
            print("\nSieving steps:")
            for prime, marked in steps:
                print(f"Marking multiples of {prime}: {marked}")
        if primes:
            print(f"\nLargest prime found: {max(primes)}")
            print(f"Average gap between primes: {(primes[-1] - primes[0]) / (len(primes) - 1):.2f}")
            
    except ValueError:
        print("Please enter a valid integer!")

if __name__ == "__main__":
    sieve_of_eratosthenes()

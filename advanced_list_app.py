def prime_numbers(n):
    return [num for num in range(2, n+1)
            if all(num % i != 0 for i in range(2, int(num**0.5)+1))]


def armstrong_numbers(n):
    return [num for num in range(1, n+1)
            if num == sum(int(digit) ** len(str(num)) for digit in str(num))]


def palindrome_numbers(n):
    return [num for num in range(1, n+1)
            if str(num) == str(num)[::-1]]


def squares(n):
    return [i**2 for i in range(1, n+1)]


def cubes(n):
    return [i**3 for i in range(1, n+1)]


def even_filter(n):
    return [i for i in range(1, n+1) if i % 2 == 0]


def odd_filter(n):
    return [i for i in range(1, n+1) if i % 2 != 0]


def main():
    n = int(input("Enter a number: "))

    print("\nPrime Numbers:", prime_numbers(n))
    print("Armstrong Numbers:", armstrong_numbers(n))
    print("Palindrome Numbers:", palindrome_numbers(n))
    print("Squares:", squares(n))
    print("Cubes:", cubes(n))
    print("Even Numbers:", even_filter(n))
    print("Odd Numbers:", odd_filter(n))


if __name__ == "__main__":
    main()

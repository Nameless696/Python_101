def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    try:
        n = int(input("Enter a positive integer: "))
        if n <= 0:
            raise ValueError("Invalid input. Please enter a positive integer.")
        result = factorial(n)
        print(f"The factorial of {n} is: {result}")
    except ValueError as e:
        print(str(e))


if __name__ == 'main':
    main()

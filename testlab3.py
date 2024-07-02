def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Example usage:
number = int(input("Enter a number: "))
result = digital_root(number)
print(f"The digital root of {number} is {result}")


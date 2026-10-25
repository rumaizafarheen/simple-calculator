
import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(a)


def power(a, b):
    return a ** b


def sine(degrees):
    return math.sin(math.radians(degrees))


def cosine(degrees):
    return math.cos(math.radians(degrees))


def tangent(degrees):
    if math.isclose(math.cos(math.radians(degrees)), 0.0, abs_tol=1e-12):
        raise ValueError("Tangent is undefined at this angle.")
    return math.tan(math.radians(degrees))


def logarithm(a):
    if a <= 0:
        raise ValueError("Logarithm requires a number greater than zero.")
    return math.log10(a)


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("\n=== Scientific Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square root")
    print("6. Power")
    print("7. Sine (degrees)")
    print("8. Cosine (degrees)")
    print("9. Tangent (degrees)")
    print("10. Logarithm (base 10)")

    choice = input("Select an operation (1-10): ").strip()

    try:
        if choice in ("1", "2", "3", "4", "6"):
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")

            operations = {
                "1": add,
                "2": subtract,
                "3": multiply,
                "4": divide,
                "6": power,
            }

            if choice not in operations:
                print("Invalid choice.")
                return

            result = operations[choice](a, b)

        elif choice in ("5", "7", "8", "9", "10"):
            a = get_number("Enter a number or angle in degrees: ")

            operations = {
                "5": square_root,
                "7": sine,
                "8": cosine,
                "9": tangent,
                "10": logarithm,
            }

            result = operations[choice](a)

        else:
            print("Invalid choice. Select a number from 1 to 10.")
            return

        print("Result:", result)

    except (ValueError, OverflowError) as error:
        print("Error:", error)


if __name__ == "__main__":
    main()




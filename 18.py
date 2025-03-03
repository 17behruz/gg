def to_decimal(number_string, base):
    """
    Converts a number string from a given base to decimal.

    Args:
        number_string: The number string in the given base.
        base: The base of the number system (2 < base < 9).

    Returns:
        The decimal equivalent of the number string. Returns -1 if input is invalid.
    """
    try:
        decimal_value = 0
        power = 0
        for digit in reversed(number_string):
            if not '0' <= digit <= '9':
                digit_value = ord(digit) - ord('A') + 10 #Handle A-F if needed. Assumes lowercase is not used
                if digit_value >= base:
                    return -1 #Invalid digit for the given base.

            else:
                digit_value = int(digit)

            if digit_value >= base:
                return -1 #Invalid digit for the given base

            decimal_value += digit_value * (base*power)
            power += 1
        return decimal_value
    except (ValueError, TypeError):
        return -1 # Handle invalid input types


# Get input from the user
number_string = input("Введите число в р-ичной системе счисления (2 < р < 9): ")
base = int(input("Введите основание системы счисления (2 < р < 9): "))

# Validate base
if not 2 < base < 9:
    print("Основание системы счисления должно быть в диапазоне (2, 9)")
else:
    # Convert to decimal and print the result
    decimal_equivalent = to_decimal(number_string, base)
    if decimal_equivalent != -1:
        print(f"Десятичный эквивалент: {decimal_equivalent}")
    else:
        print("Неверный ввод числа или основания.")


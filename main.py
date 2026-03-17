import operator
import re

# Dictionary for numbers from 0 to 99
NUMBER_WORDS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
}

# Arithmetic operations
OPERATIONS = {
    "plus": operator.add,
    "minus": operator.sub,
    "multiply": operator.mul,
    "divide": operator.truediv,
}

# Reverse mapping used to convert numbers back to words
REVERSE_WORDS = {value: word for word, value in NUMBER_WORDS.items()}


def words_to_number(text):
    """Convert English number words to a numeric value."""

    if not text or text.strip() == "":
        raise ValueError("Empty number")

    text = text.strip().lower()

    # Handle single-word numbers first.
    if text in NUMBER_WORDS:
        return NUMBER_WORDS[text]

    # Handle compound numbers such as "twenty five".
    words = text.split()
    total = 0

    for word in words:
        if word in NUMBER_WORDS:
            value = NUMBER_WORDS[word]
            if value >= 20:  # This word represents tens.
                total += value
            else:  # This word represents ones.
                total += value
        else:
            raise ValueError(f"Unknown word: {word}")

    return total


def number_to_words(number):
    """Convert a number to English words."""

    if number == 0:
        return "zero"

    if number < 0:
        return "minus " + number_to_words(abs(number))

    # Handle numbers that already exist in the dictionary.
    if number in REVERSE_WORDS:
        return REVERSE_WORDS[number]

    # Handle compound numbers.
    tens = (number // 10) * 10
    ones = number % 10

    if tens > 0 and ones > 0:
        return f"{REVERSE_WORDS[tens]} {REVERSE_WORDS[ones]}"
    elif tens > 0:
        return REVERSE_WORDS[tens]
    else:
        return REVERSE_WORDS[ones]


def parse_simple_expression(expression):
    """Parse simple expressions with two numbers and one operator."""

    expression = expression.lower().strip()

    # Find the operator.
    found_operator = None
    operator_position = -1

    for operator_word in OPERATIONS:
        if operator_word in expression:
            found_operator = operator_word
            operator_position = expression.find(operator_word)
            break

    if not found_operator:
        raise ValueError("No operator found in expression")

    # Split the expression around the operator position.
    left_text = expression[:operator_position].strip()
    right_text = expression[operator_position + len(found_operator):].strip()

    # For "multiply" and "divide", remove the leading "by" if present.
    if found_operator in ["multiply", "divide"]:
        right_text = re.sub(r"^by\s+", "", right_text)

    # An empty right-hand side is an error after cleanup.
    if not right_text:
        raise ValueError("Missing right operand")

    # Convert both operands.
    left_num = words_to_number(left_text)
    right_num = words_to_number(right_text)

    return left_num, found_operator, right_num


def calc(expression):
    """Main calculator function."""

    try:
        if not expression or expression.strip() == "":
            return "error: empty expression"

        left_num, operator_word, right_num = parse_simple_expression(expression)
        operation = OPERATIONS[operator_word]

        # Check for division by zero.
        if operator_word == "divide" and right_num == 0:
            return "error: division by zero"

        result = operation(left_num, right_num)

        # Handle floating-point results.
        if isinstance(result, float):
            if result.is_integer():
                result = int(result)
            else:
                # Round to two decimal places for simple cases.
                result = round(result, 2)

        return number_to_words(result)

    except ValueError as error:
        error_message = str(error)
        if "Unknown word" in error_message:
            unknown_word = error_message.split(": ")[1]
            return f"error: unknown word '{unknown_word}'"
        elif "No operator" in error_message:
            return "error: operator not found (use plus, minus, multiply, divide)"
        elif "Missing right operand" in error_message:
            return "error: missing right operand"
        elif "Empty number" in error_message:
            return "error: empty number"
        else:
            return f"error: {error_message}"

    except Exception:
        return "error: invalid expression format"


# Sample tests
if __name__ == "__main__":
    print("=== Basic tests ===")
    print(calc("twenty five plus thirteen"))  # thirty eight
    print(calc("five plus three"))  # eight
    print(calc("ten minus four"))  # six
    print(calc("six multiply by seven"))  # forty two
    print(calc("six multiply seven"))  # forty two (without "by")

    print("\n=== Division tests ===")
    print(calc("ten divide by two"))  # five
    print(calc("nine divide by three"))  # three
    print(calc("ten divide by zero"))  # error: division by zero
    print(calc("nine divide three"))  # three (without "by")

    print("\n=== Error tests ===")
    print(calc("five plus"))  # error: missing right operand
    print(calc("divide by five"))  # error: empty number
    print(calc("five plus unknown"))  # error: unknown word 'unknown'
    print(calc(""))  # error: empty expression

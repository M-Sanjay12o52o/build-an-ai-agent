def calculate(expression):
    """Evaluates a simple mathematical expression with two operands and one operator."""
    if not expression:
        return None

    try:
        parts = expression.split()
        if len(parts) != 3:
            raise TypeError("Invalid expression: Must contain two operands and one operator")

        operand1 = float(parts[0])
        operator = parts[1]
        operand2 = float(parts[2])

        if operator == '+':
            result = operand1 + operand2
        elif operator == '-':
            result = operand1 - operand2
        elif operator == '*':
            result = operand1 * operand2
        elif operator == '/':
            result = operand1 / operand2
        else:
            raise TypeError("Invalid operator")

        return result

    except (ValueError, TypeError) as e:
        raise TypeError(f"Invalid expression: {e}")

# Example usage
if __name__ == "__main__":
    expression = "3 + 4 * 2"  # Should evaluate to 11
    try:
        result = calculate(expression)
        print(f"The result of {expression} is: {result}")
    except TypeError as e:
        print(e)

    expression = "(3 + 4) * 2"  # Should evaluate to 14
    try:
        result = calculate(expression)
        print(f"The result of {expression} is: {result}")
    except TypeError as e:
        print(e)

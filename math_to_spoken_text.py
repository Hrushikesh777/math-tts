from latex2sympy2 import latex2sympyStr

OPERATORS_MAPPING = {
        "+": "plus",
        "-": "minus",
        "*": "times",
        "/": "divided by",
        "**": "to the power of",
        "^": "to the power of",
        "<": "less than",
        "<=": "less than or equal to",
        ">": "greater than",
        ">=": "greater than or equal to",
        "==": "equal to",
        "!=": "not equal to",
        "%": "percent",
        "=": "equals",
        "(": "open bracket",
        ")": "close bracket"
    }
    
# Add space at the start and end of each operator to handle cases where there is no space in operator and variables in expression
OPERATORS_MAPPING = {key: f" {value} " for key, value in OPERATORS_MAPPING.items()}

# Sort the operators by length to handle cases where one operator is a prefix of another
OPERATORS_MAPPING = dict(sorted(OPERATORS_MAPPING.items(), key=lambda x: len(x[0]), reverse=True))


def replace_operators_with_words(expression: str) -> str:
    # Replace the operators
    for operator in OPERATORS_MAPPING:
        word = OPERATORS_MAPPING[operator]
        expression = expression.replace(operator, word)

    # Remove extra spaces
    return " ".join(expression.split())

def latex_to_spoken_text(latex_expression: str) -> str:
    # Convert latex expression to sympy expression
    sympy_expression = latex2sympyStr(latex_expression)

    # Replace the operators with words
    spoken_text = replace_operators_with_words(sympy_expression)

    return spoken_text

if __name__ == "__main__":
    # Example usage:
    latex_expression = "\\left(7.13\\right)\\left(1.5\\right)"
    spoken_text = latex_to_spoken_text(latex_expression)
    print(spoken_text)  
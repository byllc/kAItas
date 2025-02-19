import examples 

def string_to_bin(text):
    """
    Converts a string of text to its binary representation.

    Each character in the input string is converted to an 8-bit binary number.
    The binary numbers are separated by spaces.

    Args:
        text (str): The input string to be converted.

    Returns:
        str: A string of binary numbers separated by spaces.
    """
    return examples.string_to_bin(text)


def string_to_word_tokens(string):
    """
    Tokenizes a string of text into words.

    Words are separated by spaces and punctuation is removed.

    Returns:
        list: A list of words.
    """
    return examples.string_to_word_tokens(string)
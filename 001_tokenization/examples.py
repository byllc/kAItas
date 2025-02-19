# Example functions that will pass the tests but are not necessarily
# the suggested implementation. 

def string_to_bin(text):
    return ' '.join(format(ord(char), '08b') for char in text)

def string_to_word_tokens(string):
    return [word.strip('.,?!') for word in string.split()]




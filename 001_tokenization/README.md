
# Tokenization in LLMs

Tokenization is the process of breaking down a string of text into smaller units called tokens. These tokens can be words, subwords, or even individual characters. Tokenization helps in converting text into a format that can be easily processed by machine learning models.

## Task: Write a `string_to_bin` Function

### What? 
Write a function called `string_to_bin` that converts a string to its binary representation. Each character in the input string should be converted to an 8-bit binary number, and the binary numbers should be separated by spaces. 

### Why? 
LLM's are built on a foundation of linear algebra. Fundamentally there is a lot of simple arithmetic and matrix multiplication. For this we need to have an numerical encoding of our text. We'll talk more about this in a later Kata. 

## Task: Write a `string_to_word_tokens` Function

###What? 
Tokenize a string of text into individual words. Tokens should be case sensitive. 

###Why? 
In a real model Tokens can be full words, partial words our multiple words and characters and are the fundamental building block of an LLM. 


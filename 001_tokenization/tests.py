#!/usr/bin/env python3

import unittest
import run  

class TestStringToBin(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(run.string_to_bin(''), '')

    def test_single_character(self):
        self.assertEqual(run.string_to_bin('A'), '01000001')

    def test_multiple_characters(self):
        self.assertEqual(run.string_to_bin('ABC'), '01000001 01000010 01000011')

    def test_spaces(self):
        self.assertEqual(run.string_to_bin('A B'), '01000001 00100000 01000010')

    def test_special_characters(self):
        self.assertEqual(run.string_to_bin('!@#'), '00100001 01000000 00100011')

class TestStringToWordTokens(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(run.string_to_word_tokens(''), [])

    def test_single_word(self):
        self.assertEqual(run.string_to_word_tokens('hello'), ['hello'])

    def test_multiple_words(self):
        self.assertEqual(run.string_to_word_tokens('hello world'), ['hello', 'world'])

    def test_mixed_case(self):
        self.assertNotEqual(run.string_to_word_tokens('Hello World'), ['hello', 'world'])

    def test_numbers_and_words(self):
        self.assertEqual(run.string_to_word_tokens('hello world 123'), ['hello', 'world', '123'])

if __name__ == '__main__':
    unittest.main()
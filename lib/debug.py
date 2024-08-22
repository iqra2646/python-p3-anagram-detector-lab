# lib/testing/anagram_test.py

import pytest
from anagram import Anagram

class TestAnagram:
    def test_no_anagrams(self):
        anagram = Anagram("listen")
        assert anagram.match(['google', 'banana']) == []
    
    def test_single_anagram(self):
        anagram = Anagram("listen")
        assert anagram.match(['enlists', 'google', 'inlets', 'banana']) == ['inlets']
    
    def test_multiple_anagrams(self):
        anagram = Anagram("listen")
        assert anagram.match(['inlets', 'silent', 'enlists']) == ['inlets', 'silent', 'enlists']
    
    def test_same_word(self):
        anagram = Anagram("listen")
        assert anagram.match(['listen']) == []

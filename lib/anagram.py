# your code goes here!
# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, possible_anagrams):
        # Convert the stored word into a sorted list of characters
        sorted_word = ''.join(sorted(self.word))
        
        # Initialize an empty list to store matches
        matches = []
        
        # Iterate over each word in the possible_anagrams list
        for candidate in possible_anagrams:
            # Check if the sorted characters of the candidate match the sorted_word
            if ''.join(sorted(candidate)) == sorted_word:
                matches.append(candidate)
        
        return matches

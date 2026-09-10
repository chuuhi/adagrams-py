from random import randint

def draw_letters():
    LETTER_POOL = {
        'A': 9, 
        'B': 2, 
        'C': 2, 
        'D': 4, 
        'E': 12, 
        'F': 2, 
        'G': 3, 
        'H': 2, 
        'I': 9, 
        'J': 1, 
        'K': 1, 
        'L': 4, 
        'M': 2, 
        'N': 6, 
        'O': 8, 
        'P': 2, 
        'Q': 1, 
        'R': 6, 
        'S': 4, 
        'T': 6, 
        'U': 4, 
        'V': 2, 
        'W': 2, 
        'X': 1, 
        'Y': 2, 
        'Z': 1
        }
    letters = []
    # loop through alphabet dictionary by keys to get the number value 
    for letter in LETTER_POOL:
        count = LETTER_POOL[letter]
    # add each letter to the list based on the num value
        for i in range(count):
            letters.append(letter)

    hand = []
    # loop 10 times to get a hand of 10 letters
    for i in range(10):
        random_index = randint(0, len(letters) - 1)
        hand.append(letters[random_index])
        letters.pop(random_index)
    return hand

def uses_available_letters(word, letter_bank):
    letters = []
    # check how many times this letter appears in letter_bank
    for letter in letter_bank:
        letters.append(letter)
    # check how many times this letter appears in word
    for letter in word:
        letter = letter.upper()
        if letter not in letters:
            return False
        letters.remove(letter)
    return True
    
def score_word(word):
    LETTER_VALUES = {
    "A": 1,
    "B": 3,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 4,
    "G": 2,
    "H": 4,
    "I": 1,
    "J": 8,
    "K": 5,
    "L": 1,
    "M": 3,
    "N": 1,
    "O": 1,
    "P": 3,
    "Q": 10,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "V": 4,
    "W": 4,
    "X": 8,
    "Y": 4,
    "Z": 10
}
    score = 0
    # look up letter value in dictionary
    for letter in word:
        letter = letter.upper()
        # add the correct letter value to score
        score += LETTER_VALUES[letter]
    # if word length is between 7 and 10 add 8 to score
    if 7 <= len(word) <= 10:
        score += 8

    return score

def get_highest_word_score(word_list):
    pass
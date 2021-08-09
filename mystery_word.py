import random


def mystery_word(file):
    file = open(file)
    words = file.readlines()
    file.close()

    input_level = input(' Choose your Mode: | (E)asy | (M)edium | (H)ard ')

    #Easy
    # if user chooses Easy user will get a length of 4 or less
    while input_level != "quit":
        mystery_word_list = []
        if input_level == "E" or "e":
            for word in words:
                if (len(word) >= 4 and len(word) <= 6):
                    mystery_word_list.append(word)
                    random_word = random.choice(mystery_word_list)
            break
        elif input_level == "M" or "m":
            for word in words:
                if (len(word) >= 6 and len(word) <= 8):
                    mystery_word_list.append(word)
                    random_word = random.choice(mystery_word_list)
            break
        elif input_level == "H" or "h":
            for word in words:
                if len(word) < 8:
                    mystery_word_list.append(word)
                    random_word = random.choice(mystery_word_list)
            break
    print(random_word)
        
    guess_number = 0
    guess_letter = []

    input_guess = input(' Guess a letter in your mystery word ')
    while guess_number < 8:
        if input_guess in random_word:
            guess_letter.append(input_guess)
            print(guess_letter)
        else:
            guess_number += 1
            print(guess_number)
            return("_")
        
    if guess_number == 8:
        print("game over")
#python3 mystery_word.py words.txt


mystery_word("words.txt")
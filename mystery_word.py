import random


def mystery_word(file):
    #file = open(file, 'r')
    open_file = open(file)
    words = open_file.read().split()
    #file.close()

    input_level = input(' Choose your Mode: | (E)asy | (M)edium | (H)ard ')
    
    #Easy
    # if user chooses Easy user will get a length of 4 or less
    while input_level != "quit":
        mystery_word_list = []
        if input_level == "E" or "e":
            for word in words:
                if (len(word) >= 4 and len(word) <= 6):
                    mystery_word_list.append(word)
                    random_word = random.choice(mystery_word_list).upper()
            break
        elif input_level == "M" or "m":
            for word in words:
                if (len(word) >= 6 and len(word) <= 8):
                    mystery_word_list.append(word)
                    random_word = random.choice(mystery_word_list).upper()
            break
        elif input_level == "H" or "h":
            for word in words:
                if len(word) < 8:
                    mystery_word_list.append(word)
                    random_word = random.choice(mystery_word_list).upper()
            break
    #print(random_word)
    #print(list(random_word))

    list_random_word = list(random_word)
    computer_word = list_random_word
    display_word = ["_" for letter in range(len(computer_word))]
    guess_number = 0
    guess_letter = []
    positions = []
    print("The computer word is:", computer_word)
    #print("display_word", display_word)

    while computer_word != display_word and guess_number < 8:
        print("display_word", display_word)
        input_guess = input(' Guess a letter in your mystery word ').upper()
        if input_guess in random_word:
            guess_letter.append(input_guess)
            for index in range(len(display_word)):
                if input_guess == computer_word[index]:
                    positions.append(index)
                    for position in positions:
                        display_word[position] = input_guess
                        positions = []

            print(guess_letter)
        else:
            guess_number += 1
            print(guess_number)
    if computer_word == display_word:
        print("You win!")       
    if guess_number == 8:
        print("You lose!")
#python3 mystery_word.py words.txt


mystery_word("words.txt")
import random


def mystery_word(file):
    file = open(file)
    words = file.readlines()
    file.close()
    
    #letter_guesses = []
    #number_of_guesses = 0

    input_level = input(' Choose your Mode: | (E)asy | (M)edium | (H)ard ')
    #input_guess = input(' Guess a letter in your mystery word ')

    #Easy
    # if user chooses Easy user will get a length of 4 or less
    while input_level != "quit":
        mystery_word_list = []
        if input_level == "E":
            for word in words:
                if (len(word) >= 4 and len(word) <= 6):
                    mystery_word_list.append(word)
                    random_word = random.choice(mystery_word_list)
            break
        elif input_level == "M":
            for word in words:
                if (len(word) >= 6 and len(word) <= 8):
                    mystery_word_list.append(word)
                    random_word = random.choice(mystery_word_list)
            break
        elif input_level == "H":
            for word in words:
                if len(word) > 8:
                    mystery_word_list.append(word)
                    random_word = random.choice(mystery_word_list)
            break
    print(random_word)

    #elif input_level == "M":
        #mystery_word = random.choice(medium_words)
        #print(mystery_word)
    #elif input_level == "H":
        #mystery_word = random.choice(hard_words)
        #print(mystery_word)
                #print(f"the mystery word has {len(random_word)} letters ")
                #for letter in random_word:
                   # if input_guess in random_word:
                      #  while number_of_guesses < 8:
                    
        
    #Medium
    #if user chooses Medium user will get a length of 6-8c

    #Hard
    # if user chooses Hard user will get a length of 8 or more
    #print(text)
        

#python3 mystery_word.py words.txt


mystery_word("words.txt")
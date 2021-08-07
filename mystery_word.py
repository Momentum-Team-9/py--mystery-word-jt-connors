import random

def mystery_word(file):
    file = open(file)
    text = file.read()
    text = text.split()
    random_word = random.choice(text)

    #easy = random_word(len <= 6)

    letter_guesses = []
    number_of_guesses = 0

    user_input_level = input(' Choose your difficulty: | (E)asy | (M)edium | (H)ard')
    user_input_guess = input('Guess a letter in your mystery word' )

    #Easy
    # if user chooses Easy user will get a length of 4 or less
    if user_input_level == "E":
        print(random_word)
        for letter in random_word:
            if user_input_guess in random_word:
                while number_of_guesses < 8:
                    
        
    #Medium
    #if user chooses Medium user will get a length of 6-8c

    #Hard
    # if user chooses Hard user will get a length of 8 or more
    #print(text)
                    file.close()

    #python3 mystery_word.py words.txt

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the mystery_word in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        mystery_word(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
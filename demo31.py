words = "EVAPORATE"
def play(word):
    word_completion = "_" * len(word)
    guessed = False 
    guessed_letters = []
    guessed_words = []
    print("Lets play Hangman!")
    print(word_completion)
    print("\n")
    while not guessed :
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
              print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word")
                guessed_letters.append(guess)
            else:
                print("Good job", guess, "is in the word")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print("guess is not in the word.")
                guessed_words.append(guess)
            else: 
                guessed = True
                word_completion = word
        
        else:
            print("Not a valid guess.")
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats you guessed the word! You win!")


def main():
    word = "EVAPORATE"
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = "EVAPORATE"
        play(word)

if __name__ == "__main__":
    main()

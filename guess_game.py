#This is a simple Guessing game
#Each user has 5 chances to guess the correct word

print("Guess a word for today.\n*hint: it's a tropical fruit")

the_word = "Pineapple"
guess_word = ""
guess_count = 0
guess_limit = 5
guess_is_over = False

while guess_word != the_word and not(guess_is_over):
    if guess_count < guess_limit:
        guess_word = input("Guess the word: ")
        guess_count += 1
    else:
        guess_is_over = True

if guess_is_over:
    print("You out of guesses, Sorry ")
else:
    print("You win!")
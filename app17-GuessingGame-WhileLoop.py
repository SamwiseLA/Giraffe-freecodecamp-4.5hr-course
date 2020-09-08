secret_word = "giraffe"
guess = ""
guess_limit: int = 5

while guess.lower() != secret_word and guess_limit > 0:
    guess_limit -= 1
    guess = input("Guess Word: ")
    if guess.lower() == secret_word:
        print("\n**** CONGRATULATIONS!!! You got the secret word ==> <" + guess + "> ****")
    else:
        if guess_limit < 1:
            print("\n:( You Lose :(")
        else:
            print("Nope <{0}> is not the \"Secret\" word\n\nTry Again - You have {1} more tries\n".format(guess, str(
                guess_limit)))

print("Test Format")
print("1st Var: {0}\n2nd Var: {1}".format(guess, guess_limit))

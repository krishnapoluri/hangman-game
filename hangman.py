# hangman-game
import random
name = input("What is your name: ")
print("Welcome " + name +"!\n""All The Best...")
print("Game starts now...\n")

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_again
    x = ["ball","doll","golf","secret","thief","wolf","men","death","sun","discipline"]
    word = random.choice(x)
    while word in x:
        if word=="ball":
            print("used in cricket & football")
            break
        elif word=="wolf":
            print("Animal that never been in circus")
            break
        elif word=="men":
            print("These are brave")
            break
        elif word=="death":
            print("It is inevitable")
            break
        elif word=="sun":
            print("star")
            break
        elif word=="discipline":
            print("key to continous growth")
            break
        elif word=="doll":
            print("children play with this")
            break
        elif word=="golf":
            print("billionaries sport")
            break
        elif word=="secret":
            print("hiding")
            break
        else:
            print("try your luck")
            break
    length = len(word)
    count = 
    display = '*' * length
    already_guessed = []
    play_again = ""
    hangman()

def again_play():
    global play_again
    play_again = int(input("Do you want to play again? 1 = yes, 2 = no \n"))
    while play_again not in [1, 2]:
        play_again = int(input("Do you want to play again? 1 = yes, 2 = no \n"))
    if play_again == 1:
        main()
    elif play_again == 2:
        exit()

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_again
    limit = 3
    guess = input("This is word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Enter a single LETTER onlword (Also No Numbers)\n")
        

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "*" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("you have already guessed this letter. Try another letter\n")

    else:
        count += 1

        if count == 1:
            print("Wrong input. " + str(limit - count) + " guess remaining\n")
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "|---|\n")

        elif count == 2:
            print("Wrong input. " + str(limit - count) + " guess remaining\n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "|---|\n")

        elif count == 3:
            print("Wrong input. you are hanged!\n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    .*. \n"
                  "  |   . * .\n"
                  "  |    .*. \n"
                  "  |   . * .\n"
                  "  |      \n"
                  "  |      \n"
                  "|---|\n")
            again_play()

    if word == '*' * length:
        print("Congrats! you have guessed it sussessfully...")
        again_play()

    elif count != limit:
        hangman()

main()

hangman()

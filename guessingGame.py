secret_number = 6
guess_count = 0
while guess_count<3 :
    guessed_number = int(input("Guess the number: "))
    if guessed_number==secret_number:
        print("You Won")
        break
    guess_count = guess_count + 1

else:
    print("Lost! Try Again")
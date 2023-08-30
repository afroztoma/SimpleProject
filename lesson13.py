actual_price = 20
guess_count = 0
guess_limit = 4

while guess_count < guess_limit:
    guess = int(input("Guess the number: "))
    guess_count += 1

    if guess == actual_price:
        print("You have won the game")
        break
else:
    print("Sorry,you lose the game")
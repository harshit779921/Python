secret_number = 7
guess_limit = 3

while True:
    guess_count = 0
    while guess_count < guess_limit:
        guess = int(input("Guess: "))
        guess_count += 1
        if guess == secret_number:
            print("You won!")
            break
    else:
        print("You lost!")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        break

print("Thank you for playing!")

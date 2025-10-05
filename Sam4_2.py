from random import randint

def main():
    dice = randint(1, 6)
    print(f"Die result: {dice}")

    if 5 <= dice <= 6:
        print("You win!")
    elif 3 <= dice <= 4:
        main()
    else:
        print("You lose.")
    

if __name__ == '__main__':
    main()
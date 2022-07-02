import random


def f_choice(text):
    if text in 'rps':
        return text
    else:
        print("please choose one of the letters above")
        text = f_choice(input("input: "))
        return text


def winner(you, com):
    aa = you
    bb = com
    match aa:
        case 'r':
            match bb:
                case 'r':
                    return "d", "r"
                    #print("It's a draw")
                case 'p':
                    return "L", "p"
                    #print("You loose")
                case 's':
                    return "w", "s"
                    #print("You win!")


        case 'p':
            match bb:
                case 'r':
                    return "w", "r"
                    #print("You win!")
                case 'p':
                    return "d", "p"
                    #print("It's a draw")
                case 's':
                    return "L", "s"
                    #print("You loose")

        case 's':
            match bb:
                case 'r':
                    return "L", "r"
                    #print("You loose")
                case 'p':
                    return "w", "p"
                    #print("You win!")
                case 's':
                    return "d", "s"
                    #print("It's a draw")


def play_rps(): #console gui
    print("choose r p s")
    a = f_choice(input())
    b = random.choice('rps')
    print(f"you chose {a}, computer chose {b}")
    winner(a, b)
    print("again? y/n")
    if input() == "y":
        play_rps()
    else:
        print(":(")


def rps_intg(a):#integratable function
    b = random.choice('rps')
    return winner(a, b)

print (rps_intg("r"))
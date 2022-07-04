import random


def f_choice(text):
    if text in 'rps':
        match text:
            case 'r':
                text = 1
            case 'p':
                text = 2
            case 's':
                text = 3
        return text
    else:
        print("please choose one of the letters above")
        text = f_choice(input("input: "))
        return text


def winner(a, b):
    match a:
        case 1:
            match b:
                case 1:
                    return "d", 1
                    # print("It's a draw")
                case 2:
                    return "l", 2
                    # print("You loose")
                case 3:
                    return "w", 3
                    # print("You win!")

        case 2:
            match b:
                case 1:
                    return "w", 1
                    # print("You win!")
                case 2:
                    return "d", 2
                    # print("It's a draw")
                case 3:
                    return "l", 3
                    # print("You loose")

        case 3:
            match b:
                case 1:
                    return "l", 1
                    # print("You loose")
                case 2:
                    return "w", 2
                    # print("You win!")
                case 3:
                    return "d", 3
                    # print("It's a draw")


def play_rps():  # console gui
    print("choose r p s")
    a = f_choice(input())
    b = f_choice(random.choice('rps'))
    print(f"you chose {a}, computer chose {b}")
    winner(a, b)
    print("again? y/n")
    if input() == "y":
        play_rps()
    else:
        print(":(")


def rps_intg(a):  # integratable function
    b = f_choice(random.choice('rps'))
    return winner(a, b)


#print (rps_intg(3))

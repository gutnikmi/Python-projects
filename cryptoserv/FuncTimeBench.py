from RSA import randprime, test_rsa
import time


def time_bench(func):
    count_time, result = sing_bench(func)
    res = f"Вычисление {func.__name__} заняло:{count_time}, Результат:{result} \n"
    print(res)
    with open('tst.txt', 'a') as file:
        file.write(res)


def sing_bench(func):
    tic = time.perf_counter()
    result = func()
    toc = time.perf_counter()
    count_time = round((toc - tic), 4)
    return count_time, result


def mult_bench(func_a, func_b):
    count_time_a, result_a = sing_bench(func_a)
    count_time_b, result_b = sing_bench(func_b)
    res = f"Вычисление {func_a.__name__} заняло:{count_time_a} секунд, Результат:{result_a} \nВычисление {func_b.__name__} заняло:{count_time_b} секунд, Результат:{result_b} \n"
    print(res)
    with open('tst.txt', 'a') as file:
        file.write(res)


def scoreboard():
    with open('tst.txt') as f:
        lines = f.read()
        print(lines)


def main(func_a, func_b=''):
    if func_b != '':
        print(f"1.Bench function {func_a.__name__}")
        print(f"2.Bench function {func_b.__name__}")
        print(f"3.Compare {func_a.__name__} to {func_b.__name__}")
        print("4.Print scoreboard")
        print("5.Clear scoreboard")
        a = int(input())
        match a:
            case 1:
                time_bench(func_a)
            case 2:
                time_bench(func_b)
            case 3:
                mult_bench(func_a, func_b)
            case 4:
                scoreboard()
            case 5:
                f = open('tst.txt', 'r+')
                f.truncate(0)
            case _:
                main(func_a, func_b)
        main(func_a, func_b)
    else:
        print(f"1.Bench function {func_a.__name__}")
        print("2.Print scoreboard")
        print("3.Clear scoreboard")
        a = int(input())
        if a == 1:
            time_bench(func_a)
        elif a == 2:
            scoreboard()
        elif a == 3:
            f = open('tst.txt', 'r+')
            f.truncate(0)
        else:
            main(func_a)
    main(func_a, func_b='')


if __name__ == "__main__":
    print("Welcome to TimeBench!")
    print("What do you want to do?")
    func_a = randprime
    func_b = test_rsa
    main(func_a, func_b)


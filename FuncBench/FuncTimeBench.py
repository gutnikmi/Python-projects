from RSA import randprime
import time


def time_bench(func):
    tic = time.perf_counter()
    result = func()
    toc = time.perf_counter()
    count_time = round((toc - tic), 4)
    # res = "Вычисление заняло: " + str(count_time) + ", результат: " + str(result) + "\n"
    res = f"Вычисление заняло:{count_time}, Результат:{result} \n"
    print(res)
    with open('tst.txt', 'a') as file:
        file.write(res)


def scoreboard():
    with open('tst.txt') as f:
        lines = f.read()
        print(lines)


def main(func):
    print(f"1.Bench function {func.__name__}")
    print("2.Print scoreboard")
    print("3.Clear scoreboard")
    a = int(input())
    if a == 1:
        time_bench(func)
    elif a == 2:
        scoreboard()
    elif a == 3:
        f = open('tst.txt', 'r+')
        f.truncate(0)
    main(func)


if __name__ == "__main__":
    print("Welcome to TimeBench!")
    print("What do you want to do?")
    func = randprime
    main(func)


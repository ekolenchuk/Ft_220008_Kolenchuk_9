import random
import logging

logging.basicConfig(filename="log_file.log", level=logging.INFO, filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")


def chekking_input():
    while True:
        input_str = input()
        try:
            number = int(input_str)
        except ValueError:
            print("Ошибка: Введите целое число.")
            logging.error("Введено не целое число")
            continue
        if number == 0:
            print("Ошибка: Введите число больше нуля.")
            logging.error("Введен ноль")
        elif number < 0:
            print("Ошибка: Введите положительное число.")
            logging.error("Введено отрицалельное число")
        else:
            return number


logging.info("Запуск")

print("Введите максимальное положительное число: ")
N = chekking_input()
logging.info("Введено максимальное положительное число: %s" % N)

print("Введите количество попыток (положительное число): ")
k = chekking_input()
logging.info("Введено количество попыток: %s" % k)

riddle = random.randint(1, N)
logging.info("Загадано число: %s" % riddle)

while k != 0:
    attempt = input("Введите число: ")
    try:
        attempt = int(attempt)
    except ValueError:
        print("Это вообще не число. Попытка использована.")
        logging.error("Введено не понятно что")
        k -= 1
        continue

    logging.info("Введено число: %s" % attempt)

    if attempt == riddle:
        print("Вы угадали")
        logging.info("Угадали")
        break
    elif attempt > riddle:
        print("Загаданное число меньше")
        k -= 1
    elif attempt < riddle:
        print("Загаданное число больше")
        k -= 1

if k == 0:
    print("Попытки закончились")
    logging.info("Попытки закончились")

logging.info("Программа завершена")

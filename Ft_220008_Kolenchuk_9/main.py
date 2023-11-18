import random
import logging

logging.basicConfig(filename="log_file.log", level=logging.INFO, filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("Запуск")
while True:
    try:
       N = int(input('Введите количество бочонков: '))
    except ValueError:
        print("Ошибка: Введите целое число.")
        logging.error("Введено не целое число")
        continue
    if N == 0:
        print("Ошибка: Введите число больше нуля.")
        logging.error("Введен ноль")
    elif N < 0:
        print("Ошибка: Введите положительное число.")
        logging.error("Введено отрицалельное число")
    else: break

logging.info("Введено количество чисел: %s" % (N))

pouch = [x for x in range(1,N+1)]
random.shuffle(pouch)

print('Нажмите Еnter, если "да"; "нет", чтобы закончить.')
res = []
for barrel in pouch:
    f = input('Вытащить бочонок? ')
    if f == '':
        print(barrel)
        res.append(barrel)
        logging.info("Вывод числа %s" % (barrel))
    else:
        print('Завершение...')
        logging.info("Пользователь прекратил вывод")
        break
print(*res, sep=' ')

logging.info("Программа завершена")

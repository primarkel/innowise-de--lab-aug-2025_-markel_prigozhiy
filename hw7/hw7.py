# сделаем задания аналогично дз 6: менюшкой

import random # импортируем модуль import для задания 3 угадай число

# Задание (функция) 1: список покупок
def task1():
    shopping_list = ["milk","bread", "eggs", "butter", "apples"]
    print("\n Список покупок: ")
    for i, item in enumerate (shopping_list, start=1): # enumerate ф-ия которая при переборе списка
        # дает номер и элемент, параметр strat=1 начинает не с 0 а с 1
        print(f"{i}. {item} \n")

# Задание (функция) 2: обратный отсчет
def task2():
# обработаем ошибки ввода чисел через try-except
    try:
        n = int(input("Введите число для обратного отсчета: ")) # используем ф-ию
        # int для перевода вводимого значения в число
        while n > 0: # запускаем цикл while чтобы цикл повторялся до тех пор
        # пока n не станет 0
            print(f"{n}...")
            n -= 1 # уменьшаем n на единицу чтобы n дошел 0 и мы вышли из цикла
        print("Go!\n") # \n для перехода на новую строку
    except ValueError: # ValueError - тип данных правильный, а значение неправильное
        print("Нужно ввести число!\n")

# Задание (функция) 3: угадай число
def task3():
    secr = random.randint(1, 10) # через randit генерим число
    while True: # запускаем цикл пока не угадаем число
        try:
            guess = int(input("Угадай число от 1 до 10: "))
            if guess == secr:
                print("Поздравляю! Вы угадали число!\n")
                break
            else: # если число не угадали выводим
                print("Неверно, попробуй еще раз")
        except ValueError:
            print("Нужно ввести целое число!")

# Задание (функция) 4: обработка данных
def task4():
    scores = [75, 88, -10, 95, 100, -25, 89]
    total_score = 0
    for score in scores:
        if score < 0:
            continue # игнорируем отриц значения
        elif score == 0:
            print ("Обработка прервана")
            break
        else:
            total_score += score
        print(f"Добавлен балл: {score}")
    else: # сработает если цикл завершился без break
        print("все данные успешно обработаны")
    print(f"\nИтоговая сумма баллов: {total_score}")

# Задание (функция) 5: прямоугольник
def task5():
    try:
        h = int(input("Введите высоту прямоугольника: "))
        w = int(input("Введите ширину прямоугольника: "))
        for _ in range(h):
            print("*" * w)
    except ValueError:
        print("Нужно ввести число!\n")

# главное меню
def main():
    while True:
        print("Выберите задачу: ")
        print("1 - список покупок")
        print("2 - обратный отсчет")
        print("3 - угадай число")
        print("4 - обработка данных")
        print("5 - рисуем прямоугольник")
        print("0 - выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            task1()
        elif choice == "2":
            task2()
        elif choice == "3":
            task3()
        elif choice == "4":
            task4()
        elif choice == "5":
            task5()
        elif choice == "0":
            print("выход из программы")
            break
        else: print("Неверный выбор, попробуйте снова\n")

main()




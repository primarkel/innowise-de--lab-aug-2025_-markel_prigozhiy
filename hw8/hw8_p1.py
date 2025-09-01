# Задание (функция) 1:
def task1():
    text = "Python Programming"
    print("Длина строки:", len(text)) # ф-ия len нам ищет длину строки + считает пробел за символ
    print("Символ с индексом 7:", text[7]) # в квадр скобках указываем нужный нам индекс по массиву
    # если бы нужно было 7 символ, то писали бы в скобках 6 и это был бы пробел, то есть пустая строка
    print("Последние 3 символа:", text[-3:])  # аналогично предыдущему, но используем срез
    # со значением -3 который возьмет четко последних 3 символа строки: с -3 до конца строки
    print("Содержится ли gram?:", "gram" in text) # тут работает, если есть gram то true если нету - false

# Задание (функция) 2:
def task2():
    email = " USER@DOMAIN.COM "
    email = email.strip().lower() # через метод strip убираем вокруг пробелы и чз метод lower
    # переводим строку в малый регистр
    print("Отформатированный email:", email)

    username, domain = email.split("@") # разбиваем строку чз метод split где разрывной точкой будет @
    print("Юзернейм:", username)
    print("Домен:", domain)

    print(f"Username: {username}, Domain: {domain}")

def task3():
    fruits = ["apple", "banana"]
    print("Исходный список:", fruits)

    fruits.append("orange") # чз метод append добавляем в конце списка апельсин
    print("После добавления:", fruits)
    fruits.insert(1, "grape") # чз метод insert вставялем обьект грейп на позицию 1
    print("После вставки:", fruits )
    fruits.remove("banana") # чз remove удаляем интересующий нас обьект
    print("После удаления:", fruits)
    fruits.sort() # классическая сортировка по алфавиту чз метод sort
    print("После сортировки:", fruits)
    fruits.reverse() # переворачиваем порядок элементов задом-наперед
    print("После перевороты:", fruits)

# Задание 4:
def task4():
    words = ["hello", "world", "python", "code"]

    lens = [len(word) for word in words] # создаем список длин слов чз списковое включение (короткая запись цикла)
    print("Спісок длін слов:", lens)

    word_more_four = [word for word in words if len(word) > 4] # делаем также списковое включение но уже с условием
    print("Слова больше 4 символов:", word_more_four)

    word_dic = {word: len(word) for word in words} # то же самое но оформляем чз словарь {}
    print("Словарь слов и их длин:", word_dic)

# Задание 5:
def task5():
    nums = [2, 7, 11, 15]
    target = 9
    print("пример 1:", nums, "target = ", target)

    for i in range(len(nums)): # идем по всем индексам списка
        for j in range(i+1, len(nums)): # для каждого i берем индексы справа от него
    # чтобы не повторятся и не складывать число само с собой
            if nums[i] + nums[j] == target: # проверяем дают ли эти два числа нужную нам сумму
                print("Ответ:", [i,j])

    # все аналогично для примера 2
    nums = [3, 2, 4]
    target = 6
    print("\nпример 2:", nums, "target = ", target)
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                print("Ответ:", [i, j])

# делаем опять менюшку, но уже не дикую, а умную чз словарик

menu = {
    "1": ("Операции со строкой", task1),
    "2": ("Методы строк и форматинг", task2),
    "3": ("Методы списка", task3),
    "4": ("List comprehension и словари", task4),
    "5": ("Поиск индексов по target", task5),
}

while True:
    print("\nВыберите задачу:")
    for key, value in menu.items():
        print(f"{key} - {value[0]}")
    print("0 - выход")

    choice = input("Ваш выбор: ")

    if choice == "0":
        print("выход из программы")
        break
    elif choice in menu:
        menu[choice][1]()
    else:
        print("Неверный выбор, попробуйте снова\n")



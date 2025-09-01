import datetime #импортируем модуль datetime для работы с датой и временем
# для функции show_current_time

def show_current_time():
    now = datetime.datetime.now() # получаем текущую дату и время
    print(f"Текущие дата и время:", now.strftime("%Y-%m-%d %H:%M:%S")) # форматируем дату и время в
# норм вид, идеешка сама предлагает как правильно написать

def add_vat(price, nds = 0.20): # вынесли расчет в отделбную фунцию
    return price + price * nds
def calc_prices_with_vat():
    prices = [1000, 3499, 250]
    nds = 0.20
    print("Цены с НДС:")
    for price in prices:
        print(add_vat(price, nds)) # вычисляем цену с ндс для каждой цены

menu = {
    "1": ("Показать текущую дату и время", show_current_time),
    "2": ("Рассчитать цены с НДС", calc_prices_with_vat)
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
menu = [
    {"назва": "Кава", "ціна": 25, "опис": "Свіжо зварена кава"},
    {"назва": "Апельсиновий сік", "ціна": 30, "опис": "Свіжовижатий апельсиновий сік"},
    {"назва": "Яйця з беконом", "ціна": 80, "опис": "Смажені яйця з хрустким беконом"},
    {"назва": "Панкейки з ягодами", "ціна": 60, "опис": "М’які панкейки з ягодами та медом"},
    {"назва": "Йогурт з фруктами", "ціна": 50, "опис": "Натуральний йогурт з фруктами"},

    {"назва": "Борщ", "ціна": 55, "опис": "Червоний український суп з буряком та сметаною"},
    {"назва": "Цезар", "ціна": 80, "опис": "Салат з куркою, сухариками та пармезаном"},
    {"назва": "Піца Маргарита", "ціна": 120, "опис": "Тонке тісто з томатним соусом та сиром"},
    {"назва": "Компот", "ціна": 20, "опис": "Фруктовий компот із сезонних фруктів"},
    {"назва": "Лимонад", "ціна": 25, "опис": "Освіжаючий лимонад з лимоном та м’ятою"},

    {"назва": "Курячий суп", "ціна": 50, "опис": "Легкий суп з курячим філе та овочами"},
    {"назва": "Стейк з овочами", "ціна": 150, "опис": "Соковитий яловичий стейк з овочами на грилі"},
    {"назва": "Рататуй", "ціна": 90, "опис": "Овочеве рагу з прованськими травами"},
    {"назва": "Морковний торт", "ціна": 65, "опис": "Десерт з моркви з горіхами та медовим кремом"},
    {"назва": "Трав’яний чай", "ціна": 20, "опис": "Чай з сушених трав для заспокоєння"}
]
def categorize_menu(menu_list):
    categorized = {
        "Сніданки": [],
        "Основні страви": [],
        "Напої": [],
        "Десерти": []
    }

    for item in menu_list:
        name = item["назва"].lower()

        if "кава" in name or "трав’яний чай" in name or "лимонад" in name or "компот" in name or "апельсиновий сік" in name:
            item["Категорія"] = "Напої"
        elif "морковний торт" in name or "йогурт з фруктами" in name or "панкейки з ягодами" in name:
            item["Категорія"] = "Десерти"
        elif "яйця з беконом" in name:
            item["Категорія"] = "Сніданки"
        else:
            item["Категорія"] = "Основні страви"

        categorized[item["Категорія"]].append(item)

    return categorized

def show_menu_by_category(menu_list):
    categorized = categorize_menu(menu_list)

    print("\n ==МЕНЮ ПО КАТЕГОРІЯХ ==")
    for category, items in categorized.items():
        print(f"\n {category}")
        for item in items:
            print(f" - {item ['назва']}, | {item['ціна']} грн | {item ['опис']}")

def find_dish(menu_list, name):
    for item in menu_list:
        if item["назва"].lower() == name.lower():
            return item
    return None

def edit_dish(menu_list):
    name = input("Введіть назву страви: ")
    dish = find_dish(menu_list, name)

    if dish is None:
        print("Такої страви не знайдено")
        return

    print(f"Знайдено: {dish}")
    new_price = input("Нова ціна: ")
    if new_price:
        if new_price.isdigit():
            dish["ціна"] = int(new_price)
        else:
            print("Ціна має бути числом")

    new_decs = input("Новий опис: ")
    if new_decs:
        dish["опис"] = new_decs

    new_category = input("Нова Категорія: ")
    if new_category:
        dish["Категорія"] = new_category

    print("Успішно оновлено")

def add_new_dish(menu_list):
    print("\nДодавання нової страви")
    name = input("Введіть назву: ")

    while True:
        try:
            price = float(input("Введіть ціну: "))
            if price < 0:
                print("Помилка: ціна не може бути від'ємною")
            else:
                break
        except ValueError:
            print("Будь ласка, введіть число.")

    description = input("Введіть опис: ")
    new_dish = {
        "назва": name,
        "ціна": price,
        "опис": description,
    }
    menu_list.append(new_dish)
    print(f"\n Страву '{name}' успішно додано!")

def main():
    while True:
        print(
             "\n--- СИСТЕМА КЕРУВАННЯ МЕНЮ ---\n"
             "1. Показати всі страви\n"
             "2. Додати страву\n"
             "3. Показати меню за категорією\n"
             "4. Знайти страву за назвою\n"
             "5. Додавання нової ціни\n"
             "6. Видалити страву\n"
             "7. Показати загальну ціну\n"
             "0. Вихід"
        )
        try:
            choose = int(input("Введіть цифру (0-7): "))
        except ValueError:
            print("Помилка! Вводити можна тільки цифри.")
            continue
        if choose == 1:
                print("\n" + "=" * 80)
                print(f"{'№':<3} | {'Назва':<20} | {'Ціна':<10} | {'Опис'}")
                print("-" * 80)
                for i, dish in enumerate(menu, 1):
                    print(f"{i:<3} | {dish['назва']:<20} | {dish['ціна']:>7} грн | {dish['опис']}")

                print("=" * 80 + "\n")
        elif choose == 2:
            add_new_dish(menu)
        elif choose == 3:
            show_menu_by_category(menu)
        elif choose == 4:
            name = input("Введіть назву страви: ").strip()
            dish = find_dish(menu, name)

            if dish:
                print(f"Знайдено: {dish['назва']} | {dish['ціна']} грн | {dish['опис']}")
            else:
                print("Страву не знайдено")
        elif choose == 5:
            edit_dish(menu)
            
            
     
if __name__ == "__main__":
    main()

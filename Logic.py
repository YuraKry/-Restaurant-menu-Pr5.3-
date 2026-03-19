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

def show_menu_options():
    print("\n--- СИСТЕМА КЕРУВАННЯ МЕНЮ ---")
    print("1. Показати всі страви")
    print("2. Додати страву")
    print("3. Редагувати страву")
    print("4. Видалити страву")
    print("5. Показати загальну ціну")
    print("0. Вихід")

def categorize_menu():
    categorized = {
        "Сніданки": [],
        "Основні страви": [],
        "Напої": [],
        "Десерти": []
    }

    for item in menu:
        name = item["назва"].lower()

        if "Кава" in name or "Трав’яний чай" in name or "Лимонад" in name or "Компот" in name or "Апельсиновий сік" in name:
            item["Категорія"] = "Напої"
        elif "Морковний торт" in name or "Йогурт з фруктами" in name or "Панкейки з ягодами" in name:
            item["Категорія"] = "Десерти"
        elif "Яйця з беконом" in name:
            item["Категорія"] = "Сніданки"
        else:
            item["Категорія"] = "Основні страви"

        categorized[item["Категорія"]].append(item)

    return categorized

def show_all_menu(menu_list):
    print("\n __ВСЕ МЕНЮ__")
    for item in menu_list:
        print(f"{item ['назва']}, | {item['ціна']} грн | {item ['опис']}")

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

    new_category = input("Нова категорія: ")
    if new_category:
        dish["категорія"] = new_category

    print("Успішно оновлено")

while True:
    show_menu_options()
    choice = input("Обери дію: ")

    if choice == "1":
        show_all_menu(menu)
    elif choice == "2":
        show_menu_by_category(menu)
    elif choice == "3":
        edit_dish(menu)
    elif choice == "0":
        print("Вихід.")
        break
    else:
        print("Невірний вибір!")

print("💅🏻")
def slow_print(text):
    print(text)

def show_inventory(inventory):
    if inventory:
        print(f"Инвентарь: {', '.join(inventory)}")
    else:
        print(" Инвентарь: пусто")

inventory = []

print("=" * 30)
print("   СПАСЕНИЕ КОТЕНКА")
print("=" * 30)

slow_print("Вы слышите мяуканье... Кто-то в беде!")

def park():
    print("\nПарк:")
    print("1 - Дерево (слышен мяук)")
    print("2 - Скамейка")
    print("3 - Магазин")

    show_inventory(inventory)

    choice = input("Ваш выбор (1/2/3): ")

    if choice == "1":
        tree()
    elif choice == "2":
        if "веревка" not in inventory:
            slow_print("Нашли веревку!")
            inventory.append("веревка")
        park()
    elif choice == "3":
        shop()
    else:
        park()

def tree():
    print("\nНа дереве котенок!")

    if "веревка" in inventory and "рыба" in inventory:
        slow_print("Котенок спустился по веревке за рыбой!")
        slow_print("ВЫ СПАСЛИ КОТЕНКА!")
        return

    if "веревка" in inventory:
        slow_print("Есть веревка, но котенок боится")
    elif "рыба" in inventory:
        slow_print("Есть рыба, но не достать до котенка")
    else:
        slow_print("Нужно помочь котенку спуститься")

    print("1 - Попробовать залезть")
    print("2 - Вернуться в парк")

    if input("Ваш выбор (1/2): ") == "1":
        slow_print("Не получается залезть...")
        tree()
    else:
        park()

def shop():
    print("\nМагазин:")

    if "деньги" in inventory:
        print("1 - Купить рыбу (50 руб)")
        print("2 - Вернуться")

        if input("Ваш выбор (1/2): ") == "1":
            inventory.remove("деньги")
            inventory.append("рыба")
            slow_print("Купили рыбу!")
        park()
    else:
        print("1 - Поискать деньги")
        print("2 - Вернуться")

        if input("Ваш выбор (1/2): ") == "1":
            inventory.append("деньги")
            slow_print("Нашли 50 рублей!")
        park()
park()
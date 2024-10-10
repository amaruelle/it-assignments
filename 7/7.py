# Разработать систему, реализующую CRUD операции с базой данных магазина продуктовых товаров. Работать с JSON

import json
import os

# Инициализация базы данных
def init_db():
    if not os.path.exists(os.path.join(os.path.dirname(__file__), "products.json")):
        with open(os.path.join(os.path.dirname(__file__), "products.json"), "w") as file:
            json.dump([], file)


# Создание товаров
def create_product():
    product = {}
    product["id"] = len(read_products()) + 1
    product["name"] = input("Введите название товара: ")
    
    while True:
        try:
            product["price"] = float(input("Введите цену товара: "))
            break
        except ValueError:
            print("Ошибка: цена должна быть числом.")
    
    while True:
        try:
            product["quantity"] = int(input("Введите количество товара: "))
            break
        except ValueError:
            print("Ошибка: количество должно быть целым числом.")
    return product

# Чтение товаров
def read_products():
    try:
        with open(os.path.join(os.path.dirname(__file__), "products.json"), "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
# Запись товаров
def write_products(products):
    with open(os.path.join(os.path.dirname(__file__), "products.json"), "w") as file:
        json.dump(products, file)

# CRUD операции
def create():
    products = read_products()
    product = create_product()
    products.append(product)
    write_products(products)

def read():
    products = read_products()
    for product in products:
        print(product)

def update():
    products = read_products()
    id = int(input("Введите id товара: "))
    for product in products:
        if product["id"] == id:
            product["name"] = input("Введите новое название товара: ")
            product["price"] = input("Введите новую цену товара: ")
            product["quantity"] = input("Введите новое количество товара: ")
            break
    write_products(products)

def delete():
    products = read_products()
    id = int(input("Введите id товара: "))
    for product in products:
        if product["id"] == id:
            products.remove(product)
            break
    write_products(products)

def main():
    init_db()
    while True:
        print("\n1. Создать товар")
        print("2. Просмотреть товары")
        print("3. Обновить товар")
        print("4. Удалить товар")
        print("5. Выход\n")
        choice = input("Выберите действие: ")
        if choice == "1":
            create()
        elif choice == "2":
            print("\nТовары:\n")
            read()
            print("\n")
        elif choice == "3":
            update()
        elif choice == "4":
            delete()
        elif choice == "5":
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
from inventory import Inventory, Product

def main():
    return

def check_credentials(username, password):
    with open("credentials.txt", "r") as f:
        for line in f.readlines():
            line = line.strip().split(":")
            if line[0] == username and line[1] == password:
                return True
    return False

username = input("Enter your username: ")
password = input("Enter your password: ")

if not check_credentials(username, password):
    print("Invalid username or password.")
else:
    print("Successful login!")

    # Создаем экземпляр класса Inventory и добавляем товары
    inventory = Inventory()
    with open("product.txt",'r',encoding="UTF-8") as f:
        data = f.readlines()
    for item in data:

        i=[line.rstrip('\n') for line in item.split(',')]
        inventory.add_product(Product(i[0], int(i[1]), float(i[2])))

    # inventory.add_product(Product("Яблоки", 10, 1.5))
    # inventory.add_product(Product("Груши", 5, 2.0))
    # inventory.add_product(Product("Бананы", 20, 1.0))

    # Выводим список товаров и их стоимость
    print("Список товаров на складе:")
    # print(inventory.show_inventory())
    for product_name in inventory.get_product_list():
        print("PRODUCTS",product_name.name)
        # product = inventory.find_product(product_name)
        # print(f"{product.name} ({product.quantity} шт. x {product.price}$ = {product.quantity * product.price}$)")

    # Изменяем количество товара на складе
    inventory.update_quantity("Яблоки", 5)

    # Выводим обновленный список товаров и их стоимость
    print("Список товаров на складе после изменения количества:")
    for product_name in inventory.get_product_list():
        product = inventory.find_product(product_name)
        # print(f"{product.name} ({product.quantity} шт. x {product.price}$ = {product.quantity * product.price}$)")

    # Выводим общую стоимость товаров на складе
    print(f"Общая стоимость товаров на складе: {inventory.get_total_value()}$")
main()
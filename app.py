from flask import Flask, render_template,request,redirect,url_for

from inventory import Inventory, Product
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# db = SQLAlchemy(app)

# @app.route('/')
# @app.route('/home')
# def index():
#     return render_template('index.html')
def check_credentials(username, password):
   with open("credentials.txt", "r") as f:
      for line in f.readlines():
         line = line.strip().split(":")
         if line[0] == username and line[1] == password:
            return True
   return False




@app.route('/',methods = ['POST', 'GET'])
@app.route('/home',methods = ['POST', 'GET'])
def login():
   print(request.method)
   if request.method == 'POST':
      print(request.form)
      username = request.form['uname']
      password=request.form['psw']

      if not check_credentials(username, password):
         print("Invalid username or password.")
      else:
         print("Successful login!")

         # Создаем экземпляр класса Inventory и добавляем товары
         inventory = Inventory()
         with open("product.txt", 'r', encoding="UTF-8") as f:
            data = f.readlines()
         for item in data:
            i = [line.rstrip('\n') for line in item.split(',')]
            inventory.add_product(Product(i[0], int(i[1]), float(i[2])))

         # Выводим список товаров и их стоимость
         print("Список товаров на складе:")

         for product_name in inventory.get_product_list():
            print("PRODUCTS", product_name.name)


         # Изменяем количество товара на складе
         inventory.update_quantity("Яблоки", 5)

         # Выводим обновленный список товаров и их стоимость
         print("Список товаров на складе после изменения количества:")
         for product_name in inventory.get_product_list():
            product = inventory.find_product(product_name)


         # Выводим общую стоимость товаров на складе
         print(f"Общая стоимость товаров на складе: {inventory.get_total_value()}$")
      return render_template('index.html')




   return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
class Product:
    def __init__(self, name, price, quantity=1):
        self._name = name        
        self._price = price
        self._quantity = quantity
    
    def get_total(self):
        return self._price * self._quantity
    
    def get_info(self):          
        return f"{self._name} - {self._price}₽ x {self._quantity} = {self.get_total()}₽"




class Vegetables(Product):       
    def __init__(self, name, price, quantity=1):
        super().__init__(name, price, quantity)
        self._category = "Овощи"
    
    def get_info(self):          
        return f"{self._name} - {self._price}₽/кг x {self._quantity}кг = {self.get_total()}₽"


class Grains(Product):           
    def __init__(self, name, price, quantity=1):
        super().__init__(name, price, quantity)
        self._category = "Крупы"
    
    def get_info(self):          
        return f"{self._name} - {self._price}₽ x {self._quantity}шт = {self.get_total()}₽"


class Household(Product):       
    def __init__(self, name, price, quantity=1):
        super().__init__(name, price, quantity)
        self._category = "Хоз. товары"
    
    def get_info(self):          
        return f"{self._name} - {self._price}₽ x {self._quantity}шт = {self.get_total()}₽"








class Receipt:
    def __init__(self, store_name):
        self._store_name = store_name
        self._products = []
    
    def add_product(self, product):
        self._products.append(product)
    
    def print_receipt(self):
        print("=" * 50)
        print(f"МАГАЗИН: {self._store_name}")
        print("=" * 50)
        
        total = 0
        for product in self._products:
            print(product.get_info())  # ПОЛИМОРФИЗМ
            total += product.get_total()
        
        print("=" * 50)
        print(f"ИТОГО: {total}₽")
        print(f"Товаров: {len(self._products)}")
        print("=" * 50)








vegetables = [
    Vegetables("Картофель", 45, 2),
    Vegetables("Морковь", 55, 1),
    Vegetables("Лук", 40, 1),
    Vegetables("Капуста", 60, 1),
    Vegetables("Свекла", 50, 1),
    Vegetables("Помидорчик", 180, 1),
    Vegetables("Огурцы", 150, 1),
    Vegetables("Перчик", 220, 1),
    Vegetables("Чеснок", 120, 1),
    Vegetables("Редька", 80, 1)
]



grains = [
    Grains("Ячмень", 95, 1),
    Grains("Рис", 85, 1),
    Grains("Пшено", 65, 1),
    Grains("Овсянка", 75, 1),
    Grains("Перловка", 55, 1),
    Grains("Манка", 70, 1),
    Grains("Кукурузная крупа", 60, 1),
    Grains("Крутая крупа", 50, 1),
    Grains("Рожь", 180, 1),
    Grains("Гречка зеленая", 150, 1)
]




household = [
    Household("Средство для посуды", 120, 1),
    Household("Стиральный порошок", 450, 1),
    Household("Мыло", 65, 1),
    Household("Шампунь", 280, 1),
    Household("Зубная паста", 150, 1),
    Household("Туалетная бумага", 180, 1),
    Household("Маска для волос", 120, 1),
    Household("Швабра", 190, 1),
    Household("Бальзам", 45, 1),
    Household("Мешки для мусора", 95, 1)
]




if __name__ == "__main__":
    receipt = Receipt("ПРОДУКТЫ")
    
  
    
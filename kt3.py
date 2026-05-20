# Задание 1
def print_hello(name):
    """Выводит приветствие с именем пользователя"""
    print(f"Hello, {name}!")

# Задание 2
def gcd(a, b):
    """Возвращает наибольший общий делитель двух чисел"""
    while b != 0:
        a, b = b, a % b
    return a

# ==================== тест ====================
if __name__ == "__main__":
   
    print("=== Задание 1 ===")
    string = "Yandex"
    print_hello(string)
    print()
    
   
    print("=== Задание 2 ===")
    result = gcd(12, 45)
    print(f"gcd(12, 45) = {result}")
    
   
   
    print(f"gcd(100, 50) = {gcd(100, 50)}")
    print(f"gcd(17, 19) = {gcd(17, 19)}")
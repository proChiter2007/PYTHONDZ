import random  

print("--- Задание 1 ---")
arr = list(range(1, 11))

print("Исходный массив:")
print(arr)

arr.reverse()

print("Перевернутый массив:")
print(arr)
print("\n")


print("--- Задание 2 ---")
try:
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))

 
    matrix = [[random.randint(-20, 20) for _ in range(cols)] for _ in range(rows)]

    print("\nСгенерированная матрица:")
    for row in matrix:
        print(row)


    if rows > 0 and cols > 0:
        min_element = min(min(row) for row in matrix)
        print(f"\nМинимальный элемент: {min_element}")

        if rows > 1:
            print(f"Вторая строка: {matrix[1]}")
        else:
            print("Вторая строка отсутствует (недостаточно строк).")
  
        if cols > 0:
            first_column = [row[0] for row in matrix]
            print(f"Первый столбец: {first_column}")
        else:
            print("Первый столбец отсутствует (нет столбцов).")
    else:
        print("Матрица пуста.")

except ValueError:
    print("Ошибка: введите целые числа для размера массива.")

print("\n")



print("--- Задание 3 ---")
n = 5

print(f"Введите {n} элементов массива:")

user_array = []
for _ in range(n):
    try:
        user_array.append(int(input()))
    except ValueError:
        print("Введено не число, считаем как 0")
        user_array.append(0)

has_double_zero = False

for i in range(len(user_array) - 1):
    if user_array[i] == 0 and user_array[i+1] == 0:
        has_double_zero = True
        break

if has_double_zero:
    print("В массиве есть два подряд идущих нуля.")
else:
    print("В массиве нет двух подряд идущих нулей.")

print("\n")


print("--- Задание 4 ---")
n = 10
random_array = [random.randint(1, 50) for _ in range(n)]

print(f"Массив: {random_array}")


count_div_3 = sum(1 for x in random_array if x % 3 == 0)
print(f"Количество чисел, делящихся на 3: {count_div_3}")


even_numbers = [x for x in random_array if x % 2 == 0]

if len(even_numbers) > 0:
    avg_even = sum(even_numbers) / len(even_numbers)
    
    print(f"Среднее арифметическое чётных чисел: {avg_even:.2f}")
else:
    print("В массиве нет чётных чисел, среднее вычислить нельзя.")
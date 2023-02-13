print("Введите количество операций:")
score = int(input())
print("Введите число a:")
a = float(input())
num = a
for i in range(score):
    print("Введите число b:")
    b = float(input())
    print("Введите номер операции:\n1) Вычитание\n2) Сложение\n3) Деление\n4) Умножение\n5) Возведение в степень")
    var = int(input())
    if var == 1:
        num -= b
        print(f"Итог: {num}")
        i -= 1
    elif var == 2:
        num += b
        print(f"Итог: {num}")
        i -= 1
    elif var == 3:
        if b == 0:
            print("Нельзя делить на ноль!")
            i += 1
            continue
        num = float(num / b)
        print(f"Итог: {num}")
        i -= 1
    elif var == 4:
        num *= b
        print(f"Итог: {num}")
        i -= 1
    elif var == 5:
        j = 1
        if b < 0:
            print("Нельзя возводить отрицательные числа!")
            i += 1
            continue
        st = num
        while j in range(b):
            num *= st
            j += 1
        print(f"Итог: {num}")
        i -= 1
    else:
        print("Можно ввести только 1-4!")
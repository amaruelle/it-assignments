# 7. Ввести 10 действительных чисел, вывести максимальное по абсолютной величине число.
def absolute(x):
    return x if x > 0 else -x

max_value = 0
for i in range(10):
    while True:
        try:
            num = float(input(f"Введите действительное число ({i+1}/10): "))
            break
        except ValueError:
            print("Ошибка: введите действительное число.")
    if absolute(num) > max_value:
        max_value = absolute(num)
print(f"Максимальное по абсолютной величине число: {max_value}")
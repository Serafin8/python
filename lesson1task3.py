# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
num = int(input("Введите число для произведения рассчета: "))
temp = str(num)
num1 = temp + temp
num2 = temp + temp + temp
amount = num + int(num1) + int(num2)
print("Результат: ", num, "+", num, num, "+", num, num, num, "=", amount)


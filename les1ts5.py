# Запросите у пользователя значения выручки и издержек фирмы...
prof = int(input("Укажите сумму выручки фирмы за 2020г.: "))
cos = int(input("Укажите сумму издержек фирмы за 2020 г.: "))
d = prof - cos
r = d / prof
while True:
    if d > 0:
        print("Ваша фирма имеет выручку: ", d, "у.е.")
        print("Коэф. рентабельности вашей фирмы составляет: ", r)
        print("Рассчет прибыли фирмы на одного сотрудника: ")
        empl = int(input("Укажите количество сотрудников: "))
        b = d / empl
        print("На одного сотрудника приходится: ", b, "у.е. от прибыли")
        break
    if d == 0:
        print("Ваша фирма работает без прибыли и убытков")
        break
    if d < 0:
        print("Ваша фирма работает в убыток: ", d, "у.е.")
        break

#print("Рассчет прибыли фирмы на одного сотрудника: ")
#empl = int(input("Укажите количество сотрудников: "))
#b = d / empl
#print("На одного сотрудника приходится: ", b, "у.е. от прибыли")



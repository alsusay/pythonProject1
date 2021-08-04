revenue = int(input('Введите объем выручки: '))
cost = int(input('Введите объем издержек: '))
if revenue > cost:
    profit = f"{((revenue - cost) / revenue * 100):02}"
    profit1 = revenue - cost
    stuff = int(input('Напишите, сколько сотрудников в компании: '))
    unit_profit = f"{(profit1 / stuff):02}"
    print("Ваша компания прибыльная и ее рентабельность составляет ", profit, "%")
    print("Прибыль на одного сотрудника составила", unit_profit)
else:
    print("Ваша компания несет убытки")
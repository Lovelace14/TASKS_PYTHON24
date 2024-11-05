import sys
money_capital = 20000 # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
MAX = (sys.maxsize) # Максимальное число
months = 0 # количество месяцев
for i in range(MAX):  # считаем до талого
    budget = salary + money_capital  # Обновляем бюджет

    if budget >= spend:
        months += 1  # Увеличиваем счетчик месяцев
        money_capital = budget - spend  # Обновляем подушку безопасности
        spend *= (1 + increase)  # Увеличиваем расходы на 5%
    else:
        break  # Прерываем цикл, если средств недостаточно

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", months)


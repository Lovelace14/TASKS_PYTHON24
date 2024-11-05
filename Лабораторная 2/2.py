salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
test_capital = 50000
while True:

    for i in range (10): # кол-во месяцев , которые нужно выжить
        budget = test_capital + salary
        if budget >= spend:
            test_capital = budget - spend  # Обновляем подушку безопасности
            spend *= (1 + increase)  # Увеличиваем расходы на 3%

        else :
            break  # Прерываем цикл, если средств недостаточно


    else:
        break
money_capital = 50000 - test_capital
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
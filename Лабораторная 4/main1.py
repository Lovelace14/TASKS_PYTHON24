# TODO решите задачу
import json
def task() -> float:

    #Читаем файл
    filename = 'input.json'
    with open(filename, 'r') as file:
        data = json.load(file)

    #Выполняем произведения и скалдываем их
    summa = sum(item['score'] * item['weight'] for item in data)

    # Округление результата до 3 знаков после запятой
    return round(summa, 3)

print(task())

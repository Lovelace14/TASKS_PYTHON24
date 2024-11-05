# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, razdelitel=','):
    # Разделяем участников
    participants1 = set(group1.split(razdelitel))
    participants2 = set(group2.split(razdelitel))

    # Ищем общих участников и сортируем
    common_participants = sorted(participants1 & participants2)

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой , если заменить razdelitel на |, то работает корректно
Spisok = find_common_participants(participants_first_group, participants_second_group)
print("Common :", Spisok )
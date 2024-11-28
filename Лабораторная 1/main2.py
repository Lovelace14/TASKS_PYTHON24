# TODO Найдите количество книг, которое можно разместить на дискете

# Заданные параметры
disk = 1.44
pages = 100
lines = 50
symbols = 25
bytes = 4

# Константы
bytes_in_mb = 1024 * 1024

# Рассчитываем объем одной книги и дискеты в байтах
book_size = pages * lines * symbols * bytes

disk_bytes = disk * bytes_in_mb

# Рассчитываем количество книг, которые поместятся на дискету
books = int(disk_bytes // book_size)

print("Количество книг, помещающихся на дискету:", books)

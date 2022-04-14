import time
limit = 1000
start = time.time()
with open("text.txt", "r") as file:       # Работа с файлом
    content = file.read()
    i = 0
    k = int(input('Введите число: '))
    if not content:                           # если файл пустой
        print("\nФайл text.txt является пустым.\nДобавьте не пустой файл или переименуйте существующий.")
    while i < len(content):
        if i > limit:  # условие на количество символом, которые можно прочесть
            print("\nМаксимальное количество символов было прочтено. Программа закончила работу.")
            break
        while len(content) > i and not content[i].isdigit(): #Пропускать символ, если это не цифра
            i += 1
        count = 0
        while len(content) > i and content[i].isdigit():
            count += 1
            i += 1
        if count > k and count % 2 != 0:     #Проверка на четность
            print(content[i-count:i], end = " ")
            finish = time.time()
            result = finish - start
            print("Время выполнения: " + str(result) + " секунды.")

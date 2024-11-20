# Домашнее задание по теме "Введение в потоки".

# Импорты необходимых модулей и функций
import threading
import time


# Объявление функции write_words
def write_words(word_count: int, file_name: str):
    file = open(file_name, 'w', encoding="utf-8")
    for i in range(word_count):
        file.write(f'Какое-то слово № {i+1}\n')
        time.sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл: {file_name}.')
    return


# Блок 1
start_time_1 = time.time()                                      # Взятие текущего времени

# Запуск функций с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time_1 = time.time()                                        # Взятие текущего времени
elapsed_time_1 = end_time_1 - start_time_1
print(f'Время работы функций составило: {elapsed_time_1}')      # Вывод разницы начала и конца работы функций

# Блок 2
start_time_2 = time.time()                                      # Взятие текущего времени

# Создание и запуск потоков с аргументами из задачи
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'), daemon=True)
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'), daemon=True)
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'), daemon=True)
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'), daemon=True)
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()

end_time_2 = time.time()                                        # Взятие текущего времени
elapsed_time_2 = end_time_2 - start_time_2
print(f'Время работы в потоках составило: {elapsed_time_2}')    # Вывод разницы начала и конца работы функций

# Домашнее задание по теме "Потоки на классах"

import threading
import time


class Knight(threading.Thread):                                         # Создаем класс

    def __init__(self, knight_name:str, knight_power: int):
        threading.Thread.__init__(self)
        self.name = knight_name
        self.power = knight_power

    def run(self):                                                      # Описываем поток битвы
        enemies_number = 100
        days = 0
        i = 1
        print(f'{self.name}, на нас напали!')
        while i in range(enemies_number):
            enemies_number -= self.power
            days += 1
            print(f'{self.name} сражается {days} день(дня), осталось {enemies_number} врагов.')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print(f'Все битвы закончились!')

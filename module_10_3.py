# Домашнее задание по теме "Блокировки и обработка ошибок"

import threading
import time
import random


class Bank():

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        i = 0
        while i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            deposit = random.randint(50, 500)
            self.balance += deposit
            print(f'Пополнение: {deposit}. Баланс: {self.balance}')
            time.sleep(0.001)
            i += 1

    def take(self):
        i = 0
        while i in range(100):
            withdraw = random.randint(50,100)
            print(f'Запрос выдачи на: {withdraw}.')
            if withdraw <= self.balance:
                self.balance -= withdraw
                print(f'Снятие: {withdraw}. Баланс: {self.balance}.')
            else:
                print(f'Запрос отклонен, недостаточно средств.')
                self.lock.acquire()
            i += 1


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

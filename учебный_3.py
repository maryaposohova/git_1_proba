# import threading
# import random
# import time
#
# class Bank:
#     def __init__(self):
#         self.balance = 0
#         self.lock = threading.Lock()
#
#     def deposit(self):
#         for _ in range(100):
#             random_sum = random.randint(50, 500)
#             self.lock.acquire() # захвытфваем блокировку вручную
#             try:
#                 self.balance += random_sum
#                 print(f"Пополнение: {random_sum}. Баланс: {self.balance}")
#                 if self.balance >= 500 and self.lock.locked():
#                     self.lock.release()
#             finally:
#                 if self.lock.locked():
#                     self.lock.release()
#         time.sleep(0.001)
#
#     def take(self):
#         for _ in range(100):
#             random_sum = random.randint(50, 500)
#             self.lock.acquire()  # захвытфваем блокировку вручную
#             try:
#                 print(f"Запрос на {random_sum}")
#                 if random_sum <= 500:
#                     self.balance -= random_sum
#                     print(f"Снятие: {random_sum}. Баланс: {self.balance}")
#                 if random_sum > 500:
#                     print(f"Запрос отклонён, недостаточно средств")
#             finally:
#                 if self.lock.locked():
#                     self.lock.release()
#         time.sleep(0.001)
#
# bk = Bank()
#
# # Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
# th1 = threading.Thread(target=Bank.deposit, args=(bk,))
# th2 = threading.Thread(target=Bank.take, args=(bk,))
#
# th1.start()
# th2.start()
# th1.join()
# th2.join()
#
# print(f'Итоговый баланс: {bk.balance}')


""" 2 """

# import threading
# import random
# import time
#
# class Bank:
#     def __init__(self):
#         self.balance = 0
#         self.lock = threading.Lock()  # Общая блокировка для баланса
#
#     def deposit(self):
#         for _ in range(100):
#             random_sum = random.randint(50, 500)
#             with self.lock:  # Захватываем блокировку только на время изменения баланса
#                 self.balance += random_sum
#                 print(f"Пополнение: {random_sum}. Баланс: {self.balance}")
#             time.sleep(0.001)  # Задержка вне критической секции
#
#     def take(self):
#         for _ in range(100):
#             random_sum = random.randint(50, 500)
#             with self.lock:  # Захватываем блокировку только на время изменения баланса
#                 print(f"Запрос на {random_sum}")
#                 if random_sum <= self.balance:
#                     self.balance -= random_sum
#                     print(f"Снятие: {random_sum}. Баланс: {self.balance}")
#                 else:
#                     print(f"Запрос отклонён, недостаточно средств")
#             time.sleep(0.001)  # Задержка вне критической секции
#
# # Создаем экземпляр банка
# bk = Bank()
#
# # Создаем потоки
# th1 = threading.Thread(target=bk.deposit)
# th2 = threading.Thread(target=bk.take)
#
# # Запускаем потоки
# th1.start()
# th2.start()
#
# # Ожидаем завершения потоков
# th1.join()
# th2.join()
#
# print(f'Итоговый баланс: {bk.balance}')

""" 2a """
import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()  # Общая блокировка для баланса

    def deposit(self):
        for _ in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            random_sum = random.randint(50, 500)
            with self.lock:  # Захватываем блокировку только на время изменения баланса
                self.balance += random_sum
                print(f"Пополнение: {random_sum}. Баланс: {self.balance}")
            time.sleep(0.001)  # Задержка вне критической секции

    def take(self):
        for _ in range(100):
            random_sum = random.randint(50, 500)
            with self.lock:  # Захватываем блокировку только на время изменения баланса
                print(f"Запрос на {random_sum}")
                if random_sum <= self.balance:
                    self.balance -= random_sum
                    print(f"Снятие: {random_sum}. Баланс: {self.balance}")
                else:
                    print(f"Запрос отклонён, недостаточно средств")
            time.sleep(0.003)  # Задержка вне критической секции

# Создаем экземпляр банка
bk = Bank()

# Создаем потоки
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

# Запускаем потоки
th1.start()
th2.start()

# Ожидаем завершения потоков
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')





""" 3  с гитхаба для изучения """
# import threading
# import random
# import time
# from threading import Thread, Lock
#
#
#
# class Bank(Thread):
#
#     def __init__(self):
#         super().__init__()
#         self.balance = 0
#         self.lock = Lock()
#
#     def deposit(self):
#         for i in range(100):
#             if self.balance >= 500 and self.lock.locked():
#                 self.lock.release()
#             y = random.randint(50, 500)
#             self.balance += y
#             print(f'Пополнение: {y}. Баланс: {self.balance}')
#         time.sleep(0.001)
#
#     def take(self):
#         for i in range(100):
#             x = random.randint(50,500)
#             print(f'Запрос на {x}')
#             if self.balance >= x:
#                 self.balance -= x
#                 print(f'Снятие: {x}. Баланс: {self.balance}')
#             else:
#                 print(f'Запрос отклонён, недостаточно средств')
#                 self.lock.acquire()
#         time.sleep(0.001)
#
#
# bk = Bank()
#
# th1 = threading.Thread(target=Bank.deposit, args=(bk,))
# th2 = threading.Thread(target=Bank.take, args=(bk,))
#
# th1.start()
# th2.start()
# th1.join()
# th2.join()
#
# print(f'Итоговый баланс: {bk.balance}')
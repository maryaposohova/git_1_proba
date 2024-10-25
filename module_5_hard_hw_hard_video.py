# # class User:
# #     def __init__(self, nickname, password, age: int):  # создаем условия пользователю
# #         self.nickname = nickname
# #         self.password_hash = self.hash_password(password)
# #         self.password = password
# #
# #         if age >= 18:
# #             self.age = age
# #         else:
# #             print('Вам еще нет 18 лет')
# #         print()
# #
# #     def hash_password(self, password):
# #         return password
# #
# #     def __hash__(self):
# #         return hash(self.password)
# #
# #     def __str__(self):
# #         return
#
#
# #
# # class Video:
# #     def __init__(self, title, duration, time_now, adult_mode):
# #         self.title = title   #  заголовок, строка
# #         self.duration = duration   #  продолжительность, секунды
# #         self.time_now = 0   #  секунда остановки (изначально 0)
# #         if adult_mode >= 18:
# #             if adult_mode < 18: # ограничение по возрасту, bool (False по умолчанию)
# #                 print('Вам нет 18 лет, пожалуйста покиньте страницу')
# #             else:
# #                 self.adult_mode = adult_mode
# #
#
#
# #
# #
# # class UrTube:
# #     pass
# #
# #
# # u1 = User('M', 11, 18)
# # print(u1.nickname)
# # print(u1.password_hash, id(u1.password_hash))
# # print(u1.password, id(u1.password))
# # print(u1.age)
# # u2 = Video('Video', 1000, 0, 17)
# # print(u2.title)
# # print(u2.duration)
# # print(u2.time_now)
# # print(u2.adult_mode)
# # print(1111, id(u1.password_hash))
# # print(id(hash(u1)))
#
#
# class User:
#     def __init__(self, nickname, password, age):
#         self.nickname = nickname
#         self.password = self.hash_password(password)
#         self.age = age
#
#     def hash_password(self, password):
#         return hash(password)
#
#     # def __eq__(self, other): # ==, сравниваем пароль с хеш-паролем
#     #     if isinstance(other, User):
#     #         return self.password == other.password
#
#     def __eg__(self, other):
#         return self.nickname == other.nickname
#
#     def __repr__(self, ):
#         return f'{self.nickname} {self.age}'
#
#
# class Video:
#     def __init__(self, title, duration, time_now=0, adult_mode=False):
#         self.title = title
#         self.duration = duration  # время видео в сек
#         self.time_now = time_now
#         self.adult_mode = adult_mode  # ограничение возраста
#
#     def adult_mode(self):
#         if self.adult_mode >= 18:
#             return True
#
#     def __repr__(self):
#         return f"{self.title} {self.duration} {self.time_now} {self.adult_mode}"
#
#
# class UrTube:
#     def __init__(self, users, videos, current_user):
#         self.password = None
#         self.nickname = None
#         self.users = users
#         self.videos = videos
#         self.current_user = current_user
#
#     def log_in(self, nickname, password):
#         if nickname in User and  self.password == self.hash_password(password):
#             self.nickname = self.current_user
#
#     def hash_password(self, password):
#         pass
#
#
# #
# # user1 = User('rtrt', 'gjhkk5T', 12)
# # print(user1)
# # v = Video('Masu', 200, 50, 18)
# # print(v)
#
# ur = UrTube()
# v1 = Video('Лучший язык программирования 2024 года', 200)
# v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
#
# # Добавление видео
# ur.add(v1, v2)
#
# # Проверка поиска
# print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))
#
# # Проверка на вход пользователя и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')
#
# # Проверка входа в другой аккаунт
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)
#
# # Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')

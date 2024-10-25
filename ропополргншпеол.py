# print(int.__mro__)
# print(object)


# class User:
#     __instanse = None
#     def __new__(cls, *args, **kwargs): # Он должен возвращать ссылку на класс
#         # print('Я в нью')
#         if cls.__instanse is None:     # теперь инит срабатывает с такой реализацией
#             cls.__instanse = super().__new__(cls)
#         return cls.__instanse
#
#     def __init__(self, *args, **kwargs):   # При создании нью инит уже не срабатывает, и обьект не создается, и выводится None
#         # print('Я в ините')
#         self.args = args
#         # self.kwargs = kwargs
#         # self.name = kwargs.get("name")  # достаем ключ
#         # self.age = kwargs.get("age")  #  достаем значение
#         for key, values in kwargs.items():
#             setattr(self, key, values)
#
# other = [1, 2, 3]
# user = {"name": "Denis", "age": 25, "gender": 'male' }
#
#
# user1 = User(*other, **user)
# print(user1.args)
# print(user1.name)
# print(user1.age)
# print(user1.gender)

# class MyContainer:
#
#     def __init__(self):
#         self.items = [1, 2]
#
#     def __contains__(self, item):
#         return item in self.items
#
#     def __str__(self):
#          print(f'{self.items}')
#
#
# my_container = MyContainer()
# print(my_container)

from time import sleep

# class User:
#     """
#     Класс пользователя, содержащий: имя, пароль в хешированном виде, возраст
#     """
#
#     def __init__(self, nickname, password, age):
#         self.nickname = nickname
#         self.password = self.hash_password(password)
#         self.age = age
#
#     def hash_password(self, password):
#         return hash(password)
#
#     def __str__(self):
#         return f"{self.nickname}"
#
#     def __eq__(self, other):
#         return self.nickname == other.nickname
#
#
# class Video:
#     """
#     Класс видео, содержащий: заголовок, продолжительность в сек., сек. остановки, возрастное ограничение
#     """
#
#     def __init__(self, title, duration, time_now=0, adult_mode=False):
#         self.title = title
#         self.duration = duration
#         self.time_now = time_now
#         self.adult_mode = adult_mode
#
#     def __str__(self):
#         return f"{self.title}"
#
#
# class UrTube:
#     """
#     Класс Юртуб, содержащий: список пользователей, список видео, текущий пользователь
#     """
#
#     def __init__(self, users=None, videos=None, current_user=None):
#         self.users = users if users is not None else []
#         self.videos = videos if videos is not None else []
#         self.current_user = current_user
#
#     def log_in(self, nickname, password):
#         for user in self.users:
#             if nickname == user.nickname and user.password == self.hash_password(password):
#                 self.current_user = user
#                 return f"{nickname} вошел в систему"
#         return "Неверный логин или пароль"
#
#     def log_out(self):
#         self.current_user = None
#
#     def register(self, nickname, password, age):
#         if any(user.nickname == nickname for user in self.users):
#             return f"Пользователь {nickname} уже существует"
#         user = User(nickname, password, age)
#         self.users.append(user)
#         self.log_out()
#         return self.log_in(user.nickname, password)
#
#     def add(self, *videos):
#         for video in videos:
#             if video not in self.videos:
#                 self.videos.append(video)
#
#     def get_videos(self, search_word):
#         list_search_words = [video.title for video in self.videos if search_word.lower() in video.title.lower()]
#         return list_search_words
#
#     def watch_video(self, title):
#         if not self.current_user:
#             print("Войдите в аккаунт, чтобы смотреть видео")
#             return
#
#         for video in self.videos:
#             if title == video.title:
#                 if video.adult_mode and self.current_user.age < 18:
#                     print("Вам нет 18 лет, пожалуйста покиньте страницу")
#                     return
#
#                 for sek in range(video.time_now, video.duration):
#                     print(sek + 1)
#                     sleep(1)
#                 print("Конец видео")
#                 return
#
#         print("Видео не найдено")
#
# # проверка
# ur = UrTube(1, 2, 3)
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
#



# from time import sleep
#
#
# class User:
#     """
#     Класс пользователя, содержащий: имя, пароль в хешированном виде, возраст
#     """
#
#     def __init__(self, nickname, password, age):
#         self.nickname = nickname
#         self.password = self.hash_password(password)
#         self.age = age
#
#     def hash_password(self):
#         return hash(self.password)
#
#     def __str__(self):
#         return f"{self.nickname}"
#
#     def __eq__(self, other):
#         return self.nickname == other.nickname
#
#
# print(User.__doc__)
#
#
# class Video:
#     """
#     Класс видео, содержащий:  заголовок, продолжительность в сек., сек. остановки, возр. ограничение
#     """
#
#     def __init__(self, title, duration, time_now=0, adult_mode=False):
#         self.title = title
#         self.duration = duration
#         self.time_now = time_now
#         self.adult_mode = adult_mode
#
#     def __str__(self):
#         return f"{self.title}"
#
#
# class UrTube:
#     """
#         Класс Юртуб, содержащий:  сп. польз-й., сп. видео, текущий пользователь
#
#         """
#
#     # def __init__(self, users: list, videos: list, current_user):
#     #     self.title = None
#     #     self.users = users
#     #     self.users = []
#     #     self.videos = videos
#     #     self.videos = []
#     #     self.current_user = current_user
#
#     # def __init__(self):
#     #     self.title = None
#     #     self.users = []
#     #     self.videos = []
#     #     self.current_user = None
#
#     def __init__(self, users=None, videos=None, current_user=None):
#         if not users:
#             self.users = []
#         else:
#             self.users = users
#         if not videos:
#             self.videos = []
#         else:
#             self.videos = videos
#         # self.title = None
#         self.current_user = current_user
#
#     def log_in(self, nickname, password):
#         for user in self.users:
#             if nickname == user.nickname and password == user.password:
#                 self.current_user = user
#
#     def log_out(self):  # сбросим текущего на Ноне
#         self.current_user = None
#
#     def register(self, nickname, password, age):
#         for user in self.users:
#             if nickname in self.users:
#                 return f"Пользователь {nickname} уже существует"
#             else:
#                 user = User(nickname, password, age)  # берем юзера из конструктора
#                 self.users.append(user)  # в список юзерс добавляем этого юзера
#                 self.log_out()  # обнуляем текущего юзера
#                 self.log_in(user.nickname, user.password)
#
#
#     def add(self, *videos):
#         for video in videos:
#             if video not in self.videos:
#                 self.videos.append(video)
#
#     def get_videos(self, search_word):  # приним. поисковое слово
#         list_search_words = []  # список названий с этим словом
#         for video in self.videos:
#             if search_word.lower() in video.title.lower():  # делаем все буквы в названии маленькими, как и в поск.слове
#                 list_search_words.append(video.title)  # в список слов добавляем поисковое слово
#         return list_search_words
#
#     def watch_video(self, title):
#         if not self.current_user:  # если польз не найден
#             print("Войдите в аккаунт, чтобы смотреть видео")
#             return
#         # если польз найден
#         for video in self.videos:  # пробег по видео в списке видео
#             if title in self.videos:
#                 if video.adult_mode and self.current_user.age < 18:
#                     print('Вам нет 18 лет, пожалуйста покиньте страницу')
#                     return
#                 for sek in range(video.time_now, video.duration):
#                     print(sek + 1, end=' ')
#                     time.sleep(1)
#                 print("Конец видео")
#
#
# # # проверка
# # ur = UrTube()
# # v1 = Video('Лучший язык программирования 2024 года', 200)
# # v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# #
# # # Добавление видео
# # ur.add(v1, v2)
# #
# # # Проверка поиска
# # print(1)
# # print(ur.get_videos('лучший'))
# # print(2)
# # print(ur.get_videos('ПРОГ'))
# #
# # # Проверка на вход пользователя и возрастное ограничение
# # print(3)
# # ur.watch_video('Для чего девушкам парень программист?')
# # print(4)
# # ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# # print(5)
# # ur.watch_video('Для чего девушкам парень программист?')
# # print(6)
# # ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# # print(7)
# # ur.watch_video('Для чего девушкам парень программист?')
# #
# # # Проверка входа в другой аккаунт
# # print(8)
# # ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# # print(9)
# # print(ur.current_user)
# #
# # # Попытка воспроизведения несуществующего видео
# # print(10)
# # ur.watch_video('Лучший язык программирования 2024 года!')
#
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




import time

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0

class UrTube:
    def __init__(self):
        self.videos = []
        self.current_user = None

    def add(self, *videos):
        self.videos.extend(videos)

    def register(self, username, password, age):
        self.current_user = User(username, password, age)

    def get_videos(self, search_term):
        return [video for video in self.videos if search_term.lower() in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return

                for sek in range(video.time_now, video.duration):
                    print(sek + 1, end=' ')
                    time.sleep(1)
                print("\nКонец видео")
                return

        print("Видео не найдено")

class User:
    def __init__(self, username, password, age):
        self.username = username
        self.password = password
        self.age = age

ur = UrTube()
v1 = Video('Лучший зык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.username)

ur.watch_video('Лучший язык программирования 2024 года!')


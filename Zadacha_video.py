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
# import time
#
#
# class User:
#
#     def __init__(self, nickname, age, password):
#         self.nickname = nickname
#         self.age = age
#         self.password = password
#
#     def hash_password(self):
#         return hash(self.password)
#
#     def __str__(self):
#         return f'{self.nickname}'
#
#     def __eq__(self, other):
#         return self.nickname == other.nickname
#
#
# class Video:
#     def __init__(self, title, duration, time_now=0, adult_mode=False):
#         self.title = title
#         self.duration = duration
#         self.time_now = time_now
#         self.adult_mode = adult_mode
#
#     def __str__(self):
#         return f'{self.title}'
#
#
# class UrTube:
#     def __init__(self, users=None, videos=None, current_user=None):
#         if not users:  # это True, если юзерса действительно нет (а если есть, то это будет False)
#             self.users = []
#         else:
#             self.users = users
#         if not videos:
#             self.videos = []
#         else:
#             self.videos = videos
#         self.current_user = current_user
#
#     def __str__(self):
#         return f'{self.videos}'
#
#     def log_in(self, nickname, password):
#         for user in self.users:
#             if nickname == user.nickname and hash(password) == user.hash(password):
#                 return self.current_user
#
#     def log_out(self):
#         return self.current_user is None
#
#     # def register(self, nickname, password, age):
#     #     for user in self.users:
#     #         if nickname in user.nickname:
#     #             print(f'Пользователь {nickname} уже существует')
#     #             return
#     #         user = User(nickname, password, age)
#     #         self.users.append(user)
#     #         self.log_out()
#     #         self.log_in(user.nickname, user.password)
#     def register(self, nickname, password, age):
#         for user in self.users:
#             if nickname not in user.nickname:
#                 user = User(nickname, password, age)
#                 self.users.append(user)
#                 self.log_out()
#                 self.log_in(user.nickname, user.password)
#             else:
#                 print(f'Пользователь {nickname} уже существует')
#                 return
#
#     def add(self, *args):  # добавление видео
#         if args not in self.videos:
#             for video_s in args:
#                 self.videos.append(video_s)
#
#     def get_videos(self, search_word):  # ищем видео по слову
#         lst_words = []  # пустой список для найденны названий по слову
#         for video in self.videos:
#             if search_word.lower() in video.title.lower():   # если слово есть в названии
#                 lst_words.append(video.title)   # то запис название в видео
#         return lst_words
#
#     def watch_video(self, vid):
#         if not self.current_user:  # если не вошел, то зарег-ся
#             print('Войдите в аккаунт, чтобы смотреть видео')
#             return
#
#         for video in self.videos:  # пробег по видео в списке видео
#             if vid != video.title:
#                 return
#
#             if video.adult_mode and self.current_user.age < 18:
#                 print('Вам нет 18 лет, пожалуйста покиньте страницу')
#                 return
#
#             if not video.adult_mode or video.adult_mode and self.current_user.age > 18:
#                 for sek in range(video.time_now, video.duration):
#                     print(sek + 1, end=' ')
#                     time.sleep(1)
#                 print("Конец видео")
#                 return


import time


class User:

    def __init__(self, nickname, age, password):
        self.nickname = nickname
        self.age = age
        self.password = password

    def hash_password(self):
        return hash(self.password)

    def __str__(self):
        return f'{self.nickname}'

    def __eq__(self, other):
        return self.nickname == other.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}'


class UrTube:
    def __init__(self, users=None, videos=None, current_user=None):
        if not users:  # это True, если юзерса действительно нет (а если есть, то это будет False)
            self.users = []
        else:
            self.users = users
        if not videos:
            self.videos = []
        else:
            self.videos = videos
        self.current_user = current_user

    def __str__(self):
        return f'{self.videos}'

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.hash(password):
                return self.current_user

    def log_out(self):
        return self.current_user is None

    # def register(self, nickname, password, age):
    #     for user in self.users:
    #         if nickname in user.nickname:
    #             print(f'Пользователь {nickname} уже существует')
    #             return
    #         user = User(nickname, password, age)
    #         self.users.append(user)
    #         self.log_out()
    #         self.log_in(user.nickname, user.password)
    def register(self, nickname, password, age):
        for user in self.users:
            if nickname not in user.nickname:
                user = User(nickname, password, age)
                self.users.append(user)
                self.log_out()
                self.log_in(user.nickname, user.password)
            else:
                print(f'Пользователь {nickname} уже существует')
                return

    def add(self, *args):  # добавление видео
        if args not in self.videos:
            for video_s in args:
                self.videos.append(video_s)

    def get_videos(self, search_word):  # ищем видео по слову
        lst_words = []  # пустой список для найденны названий по слову
        for video in self.videos:
            if search_word.lower() in video.title.lower():   # если слово есть в названии
                lst_words.append(video.title)   # то запис название в видео
        return lst_words

    def watch_video(self, vid):
        if not self.current_user:  # если не вошел, то зарег-ся
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for video in self.videos:  # пробег по видео в списке видео
            if vid != video.title:
                return

            if video.adult_mode and self.current_user.age < 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
                return

            if not video.adult_mode or video.adult_mode and self.current_user.age > 18:
                for sek in range(video.time_now, video.duration):
                    print(sek + 1, end=' ')
                    time.sleep(1)
                print("Конец видео")
                return

    # def watch_video(self, vid):
    #     if not self.current_user:
    #         print('Войдите в аккаунт, чтобы смотреть видео')
    #         return
    #     if self.current_user:
    #         for video in self.videos:
    #             if vid == video.title:
    #                 if video.adult_mode and self.current_user.age < 18:
    #                     print('Вам нет 18 лет, пожалуйста покиньте страницу')
    #                     return
    #
    #                 for sek in range(video.time_now, video.duration):
    #                     print(sek + 1, end=' ')
    #                     time.sleep(1)  # Эмулируем просмотр видео
    #                 print("Конец видео")
    #                 return

    # def watch_video(self, vid):
    #     if self.current_user:  # если не вошел, то зарег-ся
    #         for video in self.videos:  # пробег по видео в списке видео
    #             if vid == video.title:
    #                 for sek in range(video.time_now, video.duration):
    #                     print(sek + 1, end=' ')
    #                     time.sleep(1)
    #                     print("Конец видео")
    #                 if video.adult_mode and self.current_user.age < 18:
    #                     print('Вам нет 18 лет, пожалуйста покиньте страницу')
    #                     return
    #     else:
    #         print('Войдите в аккаунт, чтобы смотреть видео')
    #         return



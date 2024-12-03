import time


class User:

    def __init__(self, nickname, age, password):
        self.nickname = nickname
        self.age = age
        self.password = password

    def hash_password(self, password):
        return hash(self.password)

    def str(self):
        return f'{self.nickname}'

    def eg(self, other):
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
        if not current_user:
            self.current_user = current_user



    def __str__(self):
        return f'{self.videos}'

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
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

    def get_videos(self, search_word):
        lst_words = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                lst_words.append(video.title)
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
        #
    # # def watch_video(self, vid):
    # #     if self.current_user:  # если не вошел, то зарег-ся
    # #         for video in self.videos:  # пробег по видео в списке видео
    # #             if vid == video.title:
    # #                 for sek in range(video.time_now, video.duration):
    # #                     print(sek + 1, end=' ')
    # #                     time.sleep(1)
    # #                     print("Конец видео")
    # #                 if video.adult_mode and self.current_user.age < 18:
    # #                     print('Вам нет 18 лет, пожалуйста покиньте страницу')
    # #                     return
    # #     else:
    # #         print('Войдите в аккаунт, чтобы смотреть видео')
    # #         return

#
# ur = UrTube()
# v1 = Video('Лучший язык программирования 2024 года', 200)
# v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
#
# # Добавление видео
# ur.add(v1, v2)
#
# # Проверка поиска
# print(1, ur.get_videos('лучший'))
# print(2, ur.get_videos('ПРОГ'))
#
# # Проверка на вход пользователя и возрастное ограничение
# print(3)
# ur.watch_video('Для чего девушкам парень программист?')
#
#
#
# print(4)
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)   # Вам нет 18 лет, пожалуйста покиньте страницу
# ur.watch_video('Для чего девушкам парень программист?')
# print(5)
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')  # 1 2 3 4 5 6 7 8 9 10 Конец видео
#
# # Проверка входа в другой аккаунт
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(6, ur.current_user)  # Пользователь vasya_pupkin уже существует
#
# # Попытка воспроизведения несуществующего видео
# print(7)
# ur.watch_video('Лучший язык программирования 2024 года!')  # urban_pythonist

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

u = UrTube()
print(8, u.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

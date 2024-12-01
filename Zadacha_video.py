# class User:
#     def init(self, nickname, age, password):
#         self.nickname = nickname
#         self.age = age
#         self.password = hash(password)
#
#     # def hash_password(self):
#     #     return self.password
import hashlib


class User:

    def init(self, nickname, age, password):
        self.nickname = nickname
        self.age = age
        self.password = self.hash_password(password)

    def hash_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def str(self):
        return f'{self.nickname}'

    def eg(self, other):
        return self.nickname == other.nickname


# u = User('1', 1, '12')
# print(u.password) # проверка пароль отображается длинным кодом из цифр и букв
# print()


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}'


class UrTube:
    # def __init__(self, users, videos, current_user):
    #     if not users:
    #         self.users = []
    #     if not videos:
    #         self.videos = []
    #     self.current_user = current_user

    def __init__(self, users=None, videos=None, current_user=None):
        if not users:
            self.users = []
        self.users = users
        if not videos:
            self.videos = []
        self.videos = videos
        self.current_user = current_user

    # def __init__(self):
    #     users = None
    #     if not users:
    #         self.users = []
    #     videos = None
    #     if not videos:
    #         self.videos = []
    #     current_user = None
    #     self.current_user = current_user

    def __str__(self):
        return f'{self.videos}'

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                var = self.current_user == user

    # def register(self, nickname, password, age):
    #     for user in self.users:
    #         if not nickname in user.nickname:
    #             user = User(nickname, password, age)
    #             self.users.append(user)
    #             self.log_out()
    #             self.log_in(user.nickname, user.password)
    #     else:
    #         print(f'Пользователь {nickname} уже существует')
    def register(self, nickname, password, age):
        for user in self.users:
            if nickname in user.nickname:
                print(f'Пользователь {nickname} уже существует')
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.log_out()
            self.log_in(user.nickname, user.password)

    def log_out(self):
        return self.current_user is None

    def add(self, *vid):  # доб видео в видеос
        if vid not in self.videos:
            for v in vid:
                self.videos.append(v)

    def get_videos(self, word_title):
        lst_word_title = []
        for video in self.videos:
            if word_title.lower() in video.title.lower():
                word_title.append(lst_word_title)
        return lst_word_title

    def watch_video(self):
        if not self.current_user:  # если не вошел, то зарег-ся
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:  # если вошел
            for video in self.videos:
                if video == video.title:
                    if video.adult_mode and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')


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

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

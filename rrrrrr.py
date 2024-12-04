import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

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
        if not users:  # это True, если юзерс None (а если есть(т.е. не None), то это будет False)
            self.users = []
        else:
            self.users = users
        if not videos:
            self.videos = []
        else:
            self.videos = videos
        self.current_user = current_user

    def __str__(self):
        for video in self.videos:
            return f'{str(video)}'

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.hash_password():
                self.current_user = user
                # print(f'{nickname} зашел')
                return True
        return False

    def log_out(self):
        if self.current_user:
            self.current_user = None

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        user = User(nickname, password, age)
        self.users.append(user)

    # def add(self, *args):
    #     for video_s in args:
    #         if video_s not in self.videos:
    #             self.videos.append(video_s)
    def add(self, *args):  # добавление видео
        if args not in self.videos:
            for video_s in args:
                self.videos.append(video_s)

    def get_videos(self, search_word):  # ищем видео по слову
        lst_words = []  # пустой список для найденны названий по слову
        for video in self.videos:
            if search_word.lower() in video.title.lower():  # если слово есть в названии
                lst_words.append(video.title)  # то запис название в видео
        return lst_words

    def watch_video(self, vid):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for video in self.videos:
            if vid == video.title:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                if not video.adult_mode or video.adult_mode and self.current_user.age > 18:
                    for sek in range(video.time_now, video.duration):
                        print(sek + 1, end=' ')
                        time.sleep(0.5)
                    print("Конец видео")
                    return



# Пример использования
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 5)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.log_in('vasya_pupkin', 'lolkekcheburek')
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
ur.watch_video('Для чего девушкам парень программист?')
# Проверка входа в другой аккаунт
ur.log_out()
ur.log_in('vasya_pupkin', 'lolkekcheburek')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
ur.log_out()
ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
print(ur.current_user)
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

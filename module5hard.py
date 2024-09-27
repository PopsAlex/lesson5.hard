from time import sleep


class User:
    nickname = ''
    password = hash('')
    age = int()

    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = str(password)
        self.age = int(age)


class Video:
    title = ''
    duration = int()
    time_now = 0
    adult_mode = False

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    users = [{'alex': '12345'}, {'oleg': '228'}, {'lena': '1212'}]
    videos = []
    current_user = None
    need_videos = []

    def log_in(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = str(password)
        self.age = int(age)
        index = 0
        for _ in UrTube.users:
            next_keys = list(UrTube.users[index].keys())[0]
            if self.nickname == next_keys:
                next_values = list(UrTube.users[index].values())[0]
                if hash(self.password) == hash(next_values):
                    self.current_user = nickname
                    index += 1
                    break
                else:
                    index += 1
            else:
                index += 1

    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        user = {self.nickname: self.password}
        nicknames = []
        for i in UrTube.users:
            nicknames.append(i.keys())
        index = 0
        if user.keys() not in nicknames:
            UrTube.users.append(user)
            UrTube.log_in(self, self.nickname, self.password, self.age)  # оно вылазит дважды
        elif user.keys() in nicknames:
            print(f'Пользователь {nickname} уже существует')
            index += 1

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        for i in video:
            self.video = i
            if i.title not in UrTube.videos:
                UrTube.videos.append(i)
            else:
                pass

    def get_videos(self, name):
        self.name = str(name)
        index = 0
        for _ in UrTube.videos:
            if UrTube.videos[index].title in UrTube.need_videos:
                index += 1
            else:
                if self.name.lower() in UrTube.videos[index].title.lower():
                    UrTube.need_videos.append(UrTube.videos[index].title)
                else:
                    index += 1
                    print('Ваш запрос не найден')
        return UrTube.need_videos

    def watch_video(self, name):
        self.name = str(name)
        if self.current_user is not None:
            index = 0
            for _ in UrTube.videos:
                if self.name != UrTube.videos[index].title:
                    index += 1
                elif self.name == UrTube.videos[index].title:
                    if self.age >= 18:
                        # print(*range(1, UrTube.videos[index].duration + 1), 'Конец видео')
                        sleep(1)
                        for i in range(1, UrTube.videos[index].duration + 1):
                            print(i, end=' ')
                            sleep(1)
                        print('Конец видео')
                        index += 1
                        sleep(1)
                    else:
                        print('Вам нет 18 лет. Пожалуйста, покиньте страницу.')
                        index += 1
                else:
                    print('Фильм не найден')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


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
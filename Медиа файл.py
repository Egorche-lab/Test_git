# Базовый класс для любого медиа-файла
class MediaFile:
    def __init__(self, name, size, owner):
        self.name = name
        self.size = size
        self.owner = owner

    def save(self, storage):
        # сохранить файл в хранилище
        storage.upload(self)

    def delete(self, storage):
        # удалить файл из хранилища
        storage.remove(self)


# Наследники — каждый со своими метаданными
class Audio(MediaFile):
    def __init__(self, name, size, owner, duration):
        super().__init__(name, size, owner)
        self.duration = duration

    def play(self):
        print(f"Играю аудио {self.name}")

    def extract_features(self):
        # вытащить битрейт, громкость и т.п.
        pass


class Video(MediaFile):
    def __init__(self, name, size, owner, resolution):
        super().__init__(name, size, owner)
        self.resolution = resolution

    def make_preview(self):
        print(f"Делаю превью для {self.name}")

    def extract_features(self):
        # вытащить длительность, кадры и т.п.
        pass


class Image(MediaFile):
    def __init__(self, name, size, owner, width, height):
        super().__init__(name, size, owner)
        self.width = width
        self.height = height

    def resize(self, w, h):
        print(f"Меняю размер {self.name} на {w}x{h}")

    def extract_features(self):
        # вытащить цвета, лица и т.п.
        pass


# Хранилища — все с одинаковыми методами upload/remove
class LocalStorage:
    def upload(self, file):
        print(f"[local] сохраняю {file.name}")

    def remove(self, file):
        print(f"[local] удаляю {file.name}")


class S3Storage:
    def upload(self, file):
        print(f"[s3] сохраняю {file.name}")

    def remove(self, file):
        print(f"[s3] удаляю {file.name}")


class RemoteStorage:
    def upload(self, file):
        print(f"[remote] сохраняю {file.name}")

    def remove(self, file):
        print(f"[remote] удаляю {file.name}")


# ---------- Примеры ----------
song = Audio("song.mp3", 5_000_000, "egor", duration=200)
movie = Video("movie.mp4", 700_000_000, "egor", resolution="1920x1080")
photo = Image("photo.jpg", 300_000, "egor", width=800, height=600)

song.play()
movie.make_preview()
photo.resize(400, 400)

# сохраняем в разные места
song.save(LocalStorage())
movie.save(S3Storage())
photo.save(RemoteStorage())

# удаляем
song.delete(LocalStorage())
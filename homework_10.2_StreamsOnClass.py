import threading
from time import sleep

class Knight(threading.Thread):
    def __init__(self, name, skill):
        super().__init__()
        self.name = name
        self.skill = skill
        self.enemies = 100

    def run(self):
        print(f"{self.name}, на нас напали!")
        days = 0
        while self.enemies > 0:
            days += 1
            sleep(1)
            self.enemies -= self.skill
            print(f"{self.name}, сражается {days} день(дня...), осталось {max(0, self.enemies)} воинов.")
        print(f"{self.name} одержал победу спустя {days} дней!")

# Создание рыцарей
knight1 = Knight("Sir Lancelot", 10)  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20)   # Высокий уровень умения

# Запуск потоков
knight1.start()
knight2.start()

# Ожидание завершения потоков
knight1.join()
knight2.join()

print("Все битвы закончились!")
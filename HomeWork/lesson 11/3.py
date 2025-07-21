# """
#
# Описать класс Counter, реализующий целочисленный счетчик.
# который может увеличивать или уменьшать свое значение (атрибут value)
# на единицу в заданном диапазоне.
#
# Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.
#
# Определить атрибуты(свойства):
#     - value - текущее значение счетчика
#     ...
#
# Определить методы:
#     - инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
#     - increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
#     - decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
#     - reset, сбрасывает значение счетчика на стартовое
#     - метод __iter__
#     - метод __next__
#
#     * - stat, возвращает среднее количество изменений счетчика в секунду
#
# """
import time

class Counter:
    def __init__(self, start=0):
        self.value = start
        self.start = start
        self._changes = 0
        self._start_time = time.time()

    def increase(self, num=1):
        self.value += num
        self._changes += 1

    def decrease(self, num=1):
        self.value -= num
        self._changes += 1

    def reset(self):
        self.value = self.start

    def __iter__(self):
        return self

    def __next__(self):
        current = self.value
        self.increase()
        return current

    def stat(self):
        elapsed = time.time() - self._start_time
        return round(self._changes / elapsed, 2) if elapsed > 0 else 0

    def __str__(self):
        return f"Counter({self.value})"


c = Counter(5)

print(c.value)

c.increase()
c.increase(3)
c.decrease(2)

print(c.value)

c.reset()
print(c.value)

for i in c:
    print(i)
    if i > 8:
        break

print(f"Изменений в секунду: {c.stat()}")
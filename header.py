# Практическое задание №1. Вариант 7.
# 1. Опишите класс «Время» для измерения времени.
# Данные класса:
# число часов и минут.
# Конструкторы класса:
# конструктор по умолчанию, конструктор перевода из целого (часов), и конструктор произвольного времени.
# 2. Определите методы:
# приведение, если данные заданы некорректно, ввод времени,
# вывод на экран в общепринятом формате, определение значения количества минут в указанном времени от полуночи.
# 3. Объявите целое и произвольное время как статические объекты созданного типа,
# найдите значения количества минут в этих временах.
# 4. Объявите динамический объект по умолчанию, введите данные и выведите на экран.
# 5. Объявите 2-3 объекта
class time:
    def __check(self):
        return 0 < self.__hour < 24 and 0 < self.__minute < 60

    def __init__(self, hour=0, minute=0):
        self.__hour = hour
        self.__minute = minute
        if self.__check() == 0:
            self.__hour = self.__minute = 0

    def input_time(self):
        self.__hour = int(input("Введите количество часов: "))
        self.__minute = int(input("Введите количество минут: "))
        if self.__check() == 0:
            self.__hour = self.__minute = 0

    # def __str__(self):
    #     return f'Время: {self.__hour}:{self.__minute}'

    def __str__(self):
        if self.__hour < 10 and self.__minute < 10:
            return f'Время: 0{self.__hour}:0{self.__minute}'
        elif self.__hour < 10:
            return f'Время: 0{self.__hour}:{self.__minute}'
        elif self.__minute < 10:
            return f'Время: {self.__hour}:0{self.__minute}'
        else:
            return f'Время: {self.__hour}:{self.__minute}'

    def convert(self):
        return self.__minute + self.__hour * 60

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour):
        self.__hour = hour
        if self.__check() == 0:
            self.__hour = self.__minute = 0

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute):
        self.__minute = minute
        if self.__check() == 0:
            self.__hour = self.__minute = 0

"""1 Веhсия с использованием декоратора статикметод, методы проверок не приватные"""

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

    @staticmethod
    def is_valid_vin(vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not 1000000 < vin_number <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

    @staticmethod
    def is_valid_numbers(number):
        if not isinstance(number, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(number) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if IncorrectVinNumber.is_valid_vin(vin):
            self.__vin = vin
        if IncorrectCarNumbers.is_valid_numbers(numbers):
            self.__numbers = numbers

try:
    first = Car('Model1', 1000001, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')

print()

"""2 Веhсия с использованием декоратора статикметод, методы проверок приватные"""
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers


    @staticmethod
    def __is_valid_vin(vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not 1000000 < vin_number <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    @staticmethod
    def __is_valid_numbers(number):
        if not isinstance(number, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(number) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True



try:
    first = Car('Model1', 1000001, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')


import doctest

class Transport:
    def __init__(self, brand: str, max_speed: float):
        """
        Инициализация объекта "Транспортное средство".

        :param brand: Марка транспортного средства
        :param max_speed: Максимальная скорость транспортного средства
        """
        self.brand = brand
        self.max_speed = max_speed

    def move_to(self, destination: str) -> None:
        """
        Перемещение транспортного средства в указанное место.

        :param destination: Место, куда нужно переместить транспортное средство
        """
        ...

    def get_current_speed(self) -> float:
        """
        Получение текущей скорости транспортного средства.

        :return: Текущая скорость транспортного средства
        """
        ...

    def stop(self) -> None:
        """
        Остановка транспортного средства.
        """
        ...


class ElectronicDevice:
    def __init__(self, name: str, battery_level: float):
        """
        Инициализация объекта "Электронное устройство".

        :param name: Название устройства
        :param battery_level: Уровень заряда аккумулятора устройства
        """
        self.name = name
        self.battery_level = battery_level

    def turn_on(self) -> None:
        """
        Включение устройства.
        """
        ...

    def turn_off(self) -> None:
        """
        Выключение устройства.
        """
        ...

    def charge(self) -> None:
        """
        Запуск процесса зарядки устройства.
        """
        ...


class FinancialAsset:
    def __init__(self, name: str, value: float):
        """
        Инициализация объекта "Финансовый актив".

        :param name: Название актива
        :param value: Текущая стоимость актива
        """
        self.name = name
        self.value = value

    def increase_value(self, amount: float) -> None:
        """
        Увеличение стоимости актива на указанное количество.

        :param amount: Количество, на которое нужно увеличить стоимость актива
        """
        ...

    def decrease_value(self, amount: float) -> None:
        """
        Уменьшение стоимости актива на указанное количество.

        :param amount: Количество, на которое нужно уменьшить стоимость актива
        """
        ...

    def get_value(self) -> float:
        """
        Получение текущей стоимости актива.

        :return: Текущая стоимость актива
        """
        ...
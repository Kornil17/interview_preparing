from abc import ABC, abstractmethod


# Строитель может создавать различные продукты, используя один и тот же процесс строительства.
class Car:
    """
    Автомобили могут отличаться комплектацией:
    типом двигателя, количеством сидений, могут иметь или не иметь
    GPS и систему навигации и т. д. Кроме того, автомобили
    могут быть городскими, спортивными или внедорожниками.
    """


class Manual:
    """
    Руководство пользователя для данной конфигурации автомобиля.
    """


# Интерфейс строителя объявляет все возможные этапы и шаги конфигурации продукта.
class Builder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_seats(self):
        pass

    @abstractmethod
    def set_engine(self):
        pass

    @abstractmethod
    def set_trip_computer(self):
        pass

    @abstractmethod
    def set_gps(self):
        pass


# Все конкретные строители реализуют общий интерфейс по-своему.
class CarBuilder(Builder):
    def __init__(self, car: Car):
        self.car = car

    def reset(self):
        """Поместить новый объект Car в поле "car"."""
        pass

    def set_seats(self):
        """Установить указанное количество сидений."""
        pass

    def set_engine(self):
        """Установить поданный двигатель."""
        pass

    def set_trip_computer(self):
        """Установить поданную систему навигации."""
        pass

    def set_gps(self):
        """Установить или снять GPS."""
        pass

    def get_result(self) -> Car:
        """Вернуть текущий объект автомобиля."""


# В отличие от других порождающих паттернов, где продукты должны быть частью одной иерархии классов или следовать
# общему интерфейсу, строители могут создавать совершенно разные продукты, которые не имеют общего предка.
class CarManualBuilder(Builder):
    def __init__(self, manual: Manual):
        self.manual = manual

    def reset(self):
        """Поместить новый объект Manual в поле "manual".."""
        pass

    def set_seats(self):
        """Описать, сколько мест в машине."""
        pass

    def set_engine(self):
        """Добавить в руководство описание двигателя."""
        pass

    def set_trip_computer(self):
        """Добавить в руководство описание системы навигации."""
        pass

    def set_gps(self):
        """Добавить в инструкцию инструкцию GPS."""
        pass

    def get_result(self) -> Manual:
        """Вернуть текущий объект руководства."""


# Директор знает, в какой последовательности нужно заставлять работать строителя, чтобы получить ту или иную версию продукта.
# Заметьте, что директор работает со строителем через общий интерфейс, благодаря чему он не знает тип продукта, который изготовляет строитель.
class Director:
    def construct_sports_car(self, builder: Builder):
        builder.reset()
        builder.set_seats()
        builder.set_engine()
        builder.set_trip_computer()
        builder.set_gps()


# Директор получает объект конкретного строителя от клиента (приложения).
# Приложение само знает, какого строителя нужно использовать, чтобы получить определённый продукт.
class Application:
    def make_car(self):
        director = Director()
        builder = CarBuilder()
        director.construct_sports_car(builder)
        car = builder.get_result()

        manual_builder = CarManualBuilder()
        director.construct_sports_car(manual_builder)
        manual = manual_builder.get_result()


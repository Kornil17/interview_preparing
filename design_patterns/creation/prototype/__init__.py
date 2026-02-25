from abc import ABC, abstractmethod
from typing import List

class Shape(ABC):
    """
    Базовый прототип. Определяет интерфейс клонирования и
    общие поля для всех фигур.
    """

    @abstractmethod
    def clone(self) -> 'Shape':
        """
        Абстрактный метод клонирования. Должен возвращать копию объекта.
        """
        pass


class Rectangle(Shape):
    """
    Конкретный прототип — прямоугольник.
    """

    def __init__(self, source: 'Rectangle' = None):
        """
        Конструктор Rectangle. Если передан source, копирует поля родителя
        и свои собственные. Иначе инициализирует поля по умолчанию.
        """
        if source is None:
            # Обычный конструктор
            super().__init__()          # вызов конструктора Shape без параметров
            self.width: int = 0
            self.height: int = 0
        else:
            # Конструктор прототипа
            super().__init__(source)    # копируем поля из Shape
            self.width: int = source.width
            self.height: int = source.height

    def clone(self) -> Shape:
        """
        Клонирование прямоугольника: создаёт новый объект Rectangle,
        передавая в конструктор самого себя.
        """
        return Rectangle(self)


class Circle(Shape):
    """
    Конкретный прототип — окружность.
    """

    def __init__(self, source: 'Circle' = None):
        if source is None:
            super().__init__()
            self.radius: int = 0
        else:
            super().__init__(source)
            self.radius: int = source.radius

    def clone(self) -> Shape:
        return Circle(self)


class Application:
    """
    Клиентский код, использующий прототипы.
    """

    def __init__(self):
        self.shapes: List[Shape] = []

        # Создаём круг
        circle = Circle()
        circle.X = 10
        circle.Y = 10
        circle.radius = 20
        self.shapes.append(circle)

        # Клонируем круг (получаем точную копию)
        another_circle = circle.clone()
        self.shapes.append(another_circle)

        # Создаём прямоугольник
        rectangle = Rectangle()
        rectangle.width = 10
        rectangle.height = 20
        self.shapes.append(rectangle)

    def business_logic(self):
        """
        Демонстрация клонирования набора объектов без знания их конкретных классов.
        """
        shapes_copy: List[Shape] = []
        for s in self.shapes:
            shapes_copy.append(s.clone())
        # Теперь shapes_copy содержит точные копии всех элементов shapes
        return shapes_copy


# Пример использования
if __name__ == "__main__":
    app = Application()
    copies = app.business_logic()

    # Проверим, что копии действительно созданы и имеют те же атрибуты
    for original, copy in zip(app.shapes, copies):
        print(f"Оригинал: {original.__class__.__name__}, "
              f"X={original.X}, Y={original.Y}, "
              f"атрибуты: { {k:v for k,v in original.__dict__.items() if not k.startswith('_')} }")
        print(f"Копия:    {copy.__class__.__name__}, "
              f"X={copy.X}, Y={copy.Y}, "
              f"атрибуты: { {k:v for k,v in copy.__dict__.items() if not k.startswith('_')} }\n")
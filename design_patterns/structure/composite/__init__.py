from abc import ABC, abstractmethod

# Общий интерфейс компонентов.
class Graphic(ABC):
    @abstractmethod
    def move(self, x: int, y: int):
        pass

    @abstractmethod
    def draw(self):
        pass


# Простой компонент.
class Dot(Graphic):
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def move(self, x: int, y: int):
        self._x += x
        self._y += y

    def draw(self):
        """Нарисовать точку в координате X, Y."""
        pass


# Компоненты могут расширять другие компоненты.
class Circle(Dot):
    def draw(self):
        """Нарисовать окружность в координате X, Y и радиусом R."""


# Контейнер содержит операции добавления/удаления дочерних компонентов.
# Все стандартные операции интерфейса компонентов он делегирует каждому из дочерних компонентов.
class CompoundGraphic(Graphic):
    def __init__(self):
        self._children = []

    def add(self, child: Graphic):
        """Добавить компонент в список дочерних."""
        self._children.append(child)

    def remove(self, child: Graphic):
        """Убрать компонент из списка дочерних."""
        self._children.remove(self._children.index(child))

    def move(self, x: int, y: int):
        for child in self._children:
            child.move()

    def draw(self):
        """1. Для каждого дочернего компонента:
            - Отрисовать компонент.
            - Определить координаты максимальной границы.
        2. Нарисовать пунктирную границу вокруг всей области."""
        pass


# Приложение работает единообразно как с единичными компонентами, так и с целыми группами компонентов.
class ImageEditor:
    def __init__(self, all: CompoundGraphic):
        self._all = all

    def load(self):
        self._all.add(Dot(1, 3))
        self._all.add(Circle(3, 3))

    def group_selected(self, components: list[Graphic]):
        """Группировка выбранных компонентов в один сложный компонент."""
        group = CompoundGraphic()
        for component in components:
            group.add(component)
            self._all.remove(component)
        self._all.add(group)
        self._all.draw()


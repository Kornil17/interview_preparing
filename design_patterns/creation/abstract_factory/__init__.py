from abc import ABC, abstractmethod

# Этот паттерн предполагает, что у вас есть несколько семейств
# продуктов, находящихся в отдельных иерархиях классов (Button/Checkbox).
# Продукты одного семейства должны иметь общий интерфейс.
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

# Семейства продуктов имеют те же вариации (macOS/Windows).
class WinButton(Button):
    def paint(self):
        """Отрисовать кнопку в стиле Windows."""
        pass


class MacButton(Button):
    def paint(self):
        """Отрисовать кнопку в стиле macOS."""
        pass


class CheckBox(ABC):
    @abstractmethod
    def paint(self):
        pass


class WinCheckbox(CheckBox):
    def paint(self):
        """Отрисовать чекбокс в стиле Windows."""
        pass


class MacCheckbox(CheckBox):
    def paint(self):
        """Отрисовать чекбокс в стиле macOS."""
        pass


# Абстрактная фабрика знает обо всех абстрактных типах продуктов.
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> CheckBox:
        pass


# Каждая конкретная фабрика знает и создаёт только продукты своей вариации.
# Несмотря на то, что фабрики оперируют конкретными классами, их методы возвращают абстрактные типы продуктов.
# Благодаря этому фабрики можно взаимозаменять, не изменяя клиентский код.
class WinFactory(GUIFactory):
    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> CheckBox:
        return WinCheckbox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> CheckBox:
        return MacCheckbox()


# Для кода, использующего фабрику, не важно, с какой конкретно фабрикой он работает.
# Все получатели продуктов работают с ними через общие интерфейсы.
class Application:

    def __init__(self, factory: GUIFactory):
        self.button = None
        self.factory = factory

    def create_ui(self):
        self.button = self.factory.create_button()

    def paint(self):
        return self.button.paint()


# Приложение выбирает тип конкретной фабрики и создаёт её динамически, исходя из конфигурации или окружения.
class ApplicationConfigurator:
    def main(self):
        config = {}
        if config["os"] == "win":
            factory = WinFactory()
        elif config["os"] == "mac":
            factory = MacFactory()
        else:
            raise Exception

        app = Application(factory)
        return app
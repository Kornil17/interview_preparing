from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def on_click(self, f):
        pass


class WindowsButton(Button):
    def render(self):
        """Отрисовать кнопку в стиле Windows."""

    def on_click(self, f):
        """Навесить на кнопку обработчик событий Windows."""


class HTMLButton(Button):
    def render(self):
        """Вернуть HTML-код кнопки."""

    def on_click(self, f):
        """Навесить на кнопку обработчик события браузера."""


class Dialog(ABC):
    """Базовый класс фабрики. Заметьте, что "фабрика" — это всего лишь дополнительная роль для класса.
    Скорее всего, он уже имеет какую-то бизнес-логику, в которой требуется создание разнообразных продуктов."""

    def render(self):
        """Чтобы использовать фабричный метод, вы должны убедиться в том,
        что эта бизнес-логика не зависит от конкретных классов продуктов.
        Button — это общий интерфейс кнопок, поэтому все хорошо."""
        ok_button = self.create_button()
        ok_button.on_click()
        ok_button.render()

    @abstractmethod
    def create_button(self) -> Button:
        """Конкретные фабрики переопределяют фабричный метод и возвращают из него собственные продукты."""


class WindowsDialog(Dialog):
    def create_button(self):
        return WindowsButton()


class WebDialog(Dialog):
    def create_button(self):
        return HTMLButton()


class Application:
    def __init__(self):
        config = self.read_config()

        if config["os"] == "Windows":
            self.dialog = WindowsDialog()
        elif config["os"] == "Web":
            self.dialog = WebDialog()
        else:
            raise NotImplementedError()

    def read_config(self):
        return {}

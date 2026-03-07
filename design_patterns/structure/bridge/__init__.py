from abc import ABC, abstractmethod


# Все устройства имеют общий интерфейс.
# Поэтому с ними может работать любой пульт.
class IDevice(ABC):
    """Класс интерфейс для реализации устройств."""

    @abstractmethod
    def is_enabled(self):
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def get_volume(self):
        pass

    @abstractmethod
    def set_volume(self, percent: int):
        pass

    @abstractmethod
    def get_channel(self):
        pass

    @abstractmethod
    def set_channel(self, channel: int):
        pass


# Но каждое устройство имеет особую реализацию.
class Tv(IDevice):
    pass


class Radio(IDevice):
    pass


# Класс пультов имеет ссылку на устройство, которым управляет.
# Методы этого класса делегируют работу методам связанного устройства.
class Remote(ABC):
    """Класс асбтракция для реализации управления устройствами."""

    def __init__(self, device: IDevice):
        self._device = device

    def toggle_power(self):
        if self._device.is_enabled():
            self._device.disable()
        else:
            self._device.enable()

    def volume_down(self):
        self._device.set_volume(self._device.get_volume() - 10)

    def volume_up(self):
        self._device.set_volume(self._device.get_volume() + 10)

    def channel_down(self):
        self._device.set_channel(self._device.get_channel() - 1)

    def channel_up(self):
        self._device.set_channel(self._device.get_channel() + 1)


# Вы можете расширять класс пультов, не трогая код устройств.
class AdvanceRemote(Remote):
    def mute(self):
        self._device.set_volume(0)



# Клиентский код
tv = Tv()
remote = Remote(tv)
remote.toggle_power()

radio = Radio()
advance_remote = AdvanceRemote(radio)
advance_remote.mute()

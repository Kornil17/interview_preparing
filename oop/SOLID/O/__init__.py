# Класс заказов имеет метод расчёта стоимости доставки, причём способы доставки «зашиты» непосредственно в самметод.
# Если вам нужно будет добавить новый способ доставки, то придётся трогать весь класс Order

# ДО: код класса заказа нужно будет изменять при добавлении нового способа доставки.

from dataclasses import dataclass

@dataclass(slots=True, kw_only=True, frozen=True)
class Order:
    line_items: list[str]
    shipping: str

    def get_total(self):
        pass

    def get_total_weight(self):
        pass

    def get_shipping_cost(self):
        if self.shipping == "ground":
            if self.get_total() > 100:
                return
            return max(10, self.get_total_weight() * 1.5)

        if self.shipping == "air":
            return max(20, self.get_total_weight() * 3)


# Проблему можно решить, если применить паттерн Стратегия.
# Для этого нужно выделить способы доставки в собственные классы с общим интерфейсом.


# ПОСЛЕ: новые способы доставки можно добавить, не трогая класс заказов.

# Теперь при добавлении нового способа доставки нужно будет реализовать новый класс интерфейса доставки, не трогая класс заказов.
# Объект способа доставки в класс заказа будет подавать клиентский код, который раньше устанавливал способ доставки простой строкой.
# Бонус этого решения в том, что расчёт времени и даты доставки тоже можно поместить в новые классы, повинуясь принципу единственной ответственности.


from dataclasses import dataclass


class IShipping:
    def get_cost(self):
        pass

    def get_date(self):
        pass


@dataclass(slots=True, kw_only=True, frozen=True)
class Ground:
    def get_cost(self, order):
        return max(10, order.get_total_weight() * 1.5)

    def get_date(self):
        pass


@dataclass(slots=True, kw_only=True, frozen=True)
class Air:
    def get_cost(self, order):
        return max(20, order.get_total_weight() * 3)

    def get_date(self):
        pass


@dataclass(slots=True, kw_only=True, frozen=True)
class Order:
    line_items: list[str]
    shipping: IShipping

    def get_total(self):
        pass

    def get_total_weight(self):
        pass

    def get_shipping_cost(self):
        return self.shipping.get_cost(order=self)

# Класс Employee имеет сразу несколько причин для изменения.
# Первая связана с основной задачей класса — управлением данными сотрудника.
# Но есть и вторая: изменения, связанные с форматированием отчёта для печати, будут затрагивать класс сотрудников.


# ДО: класс сотрудника содержит разнородные поведения.
from dataclasses import dataclass

@dataclass(frozen=True, slots=True, kw_only=True)
class Employee:
    name: str

    def get_name(self):
        pass

    def print_time_sheet_report(self):
        pass


# Проблему можно решить, выделив операцию печати в отдельный класс.

# ПОСЛЕ: лишнее поведение переехало в собственный класс.

@dataclass(frozen=True, slots=True, kw_only=True)
class Employee:
    name: str

    def get_name(self):
        pass


@dataclass(frozen=True, slots=True, kw_only=True)
class TimeSheetReport:
    def print_time_sheet_report(self):
        pass


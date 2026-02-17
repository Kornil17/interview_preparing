# В этом примере высокоуровневый класс формирования бюджетных отчётов напрямую использует класс базы данных для загрузки и сохранения своей информации.
# ДО: высокоуровневый класс зависит от низкоуровневого.

from dataclasses import dataclass


@dataclass(slots=True, kw_only=True, frozen=True)
class MySQLDatabase:
    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


@dataclass(slots=True, kw_only=True, frozen=True)
class BudgetReport:
    database: MySQLDatabase

    def open(self, date: str):
        pass

    def save(self):
        pass


# ---

# Вы можете исправить проблему, создав высокоуровневый интерфейс для загрузки/сохранения данных и привязав к нему класс отчётов.
# Низкоуровневые классы должны реализовать этот интерфейс, чтобы их объекты можно было использовать внутри объекта отчётов.

# Таким образом, меняется направление зависимости.
# Если раньше высокий уровень зависел от низкого, то сейчас всё наоборот — низкоуровневые классы зависят от высокоуровневого интерфейса.

# ПОСЛЕ: низкоуровневые классы зависят от высокоуровневой абстракции.


@dataclass(slots=True, kw_only=True, frozen=True)
class Database:
    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


@dataclass(slots=True, kw_only=True, frozen=True)
class MySQLDatabase(Database):
    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


@dataclass(slots=True, kw_only=True, frozen=True)
class MongoDBDatabase(Database):
    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


@dataclass(slots=True, kw_only=True, frozen=True)
class BudgetReport:
    database: Database

    def open(self, date: str):
        pass

    def save(self):
        pass

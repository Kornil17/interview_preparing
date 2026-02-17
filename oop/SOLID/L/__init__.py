# пример неудачной иерархии классов документов.

# ДО: подкласс «обнуляет» работу базового метода.

from dataclasses import dataclass


@dataclass(slots=True, kw_only=True, frozen=True)
class Document:
    data: str
    filename: str

    def open(self):
        pass

    def save(self):
        pass


@dataclass(slots=True, kw_only=True, frozen=True)
class ReadOnlyDocument(Document):
    def save(self):
        raise Exception("Unable to save RO file")


@dataclass(slots=True, kw_only=True, frozen=True)
class Project:
    documents: Document

    def open_all(self):
        for doc in self.documents:
            doc.open()

    def save_all(self):
        for doc in self.documents:
            doc.save()

# Метод сохранения в подклассе ReadOnlyDocuments выбросит исключение, если кто-то попытается вызвать его метод сохранения.
# Базовый метод не имеет такого ограничения.
# Из-за этого клиентский код вынужден проверять тип документа при сохранении всех документов.

# При этом нарушается ещё и принцип открытости/закрытости, так как клиентский код начинает зависеть от конкретного класса, который нельзя заменить на другой, не внося изменений в клиентский код.


# ----

# Проблему можно решить, перепроектировав иерархию классов.
# Базовый класс сможет только открывать документы, но не сохранять их.
# Подкласс, который теперь будет называться WritableDocument , расширит поведение родителя, позволив сохранять документ.

@dataclass(slots=True, kw_only=True, frozen=True)
class Document:
    data: str
    filename: str

    def open(self):
        pass

    def save(self):
        pass


@dataclass(slots=True, kw_only=True, frozen=True)
class WritableDocument(Document):
    def save(self):
        pass


@dataclass(slots=True, kw_only=True, frozen=True)
class Project:
    all_docs: Document
    writable_docs: Document

    def open_all(self):
        for doc in self.all_docs:
            doc.open()

    def save_all(self):
        for doc in self.writable_docs:
            doc.save()


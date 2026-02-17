# Представьте библиотеку для работы с облачными провайдерами.
# В первой версии она поддерживала только Amazon, имеющий полный набор облачных услуг.
# Исходя из них и проектировался интерфейс будущих классов.
# Но позже стало ясно, что получившийся интерфейс облачного провайдера слишком широк, так как есть другие провайдеры, реализующие только часть из всех возможных сервисов.

# ДО: не все клиенты могут реализовать операции интерфейса.

from dataclasses import dataclass


@dataclass(slots=True, kw_only=True, frozen=True)
class CloudProvider:
    def store_file(self, name):
        pass

    def get_file(self, name):
        pass

    def create_server(self, region):
        pass

    def list_servers(self, region):
        pass

    def get_cdn_address(self):
        pass


@dataclass(slots=True, kw_only=True, frozen=True)
class Amazon(CloudProvider):
    def store_file(self, name):
        pass

    def get_file(self, name):
        pass

    def create_server(self, region):
        pass

    def list_servers(self, region):
        pass

    def get_cdn_address(self):
        pass


@dataclass(slots=True, kw_only=True, frozen=True)
class DropBox(CloudProvider):
    def store_file(self, name):
        pass

    def get_file(self, name):
        pass

    def create_server(self, region):
        raise NotImplemented

    def list_servers(self, region):
        raise NotImplemented

    def get_cdn_address(self):
        raise NotImplemented


# Чтобы не плодить классы с пустой реализацией, раздутый интерфейс можно разбить на части.
# Классы, которые были способны реализовать все операции старого интерфейса, могут реализовать сразу несколько новых частичных интерфейсов.

@dataclass(slots=True, kw_only=True, frozen=True)
class CloudHostingProvider:
    def create_server(self, region):
        pass

    def list_servers(self, region):
        pass


@dataclass(slots=True, kw_only=True, frozen=True)
class CDNProvider:
    def get_cdn_address(self):
        pass


@dataclass(slots=True, kw_only=True, frozen=True)
class CloudStorageProvider:
    def store_file(self, name):
        pass

    def get_file(self, name):
        pass



@dataclass(slots=True, kw_only=True, frozen=True)
class Amazon(CloudHostingProvider, CDNProvider, CloudStorageProvider):
    def store_file(self, name):
        pass

    def get_file(self, name):
        pass

    def create_server(self, region):
        pass

    def list_servers(self, region):
        pass

    def get_cdn_address(self):
        pass


@dataclass(slots=True, kw_only=True, frozen=True)
class DropBox(CloudStorageProvider):
    def store_file(self, name):
        pass

    def get_file(self, name):
        pass


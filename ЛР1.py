from abc import ABC, abstractmethod
from typing import Any
import doctest


class PhysicalObject(ABC):
    """
    Абстрактный класс, описывающий физический объект.
    """

    def __init__(self, weight: float, material: str) -> None:
        """
        :param weight: Масса объекта в килограммах (должна быть > 0)
        :param material: Материал объекта (непустая строка)
        """
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом")
        if not material:
            raise ValueError("Материал не может быть пустым")

        self.weight: float = weight
        self.material: str = material

    @abstractmethod
    def move(self, distance: float) -> None:
        """
        Перемещает объект на заданное расстояние.

        :param distance: Расстояние в метрах (должно быть > 0)
        :return: None

        >>> class Box(PhysicalObject):
        ...     def move(self, distance: float) -> None:
        ...         pass
        ...     def break_object(self) -> None:
        ...         pass
        >>> box = Box(2.5, "wood")
        >>> box.move(3.0)
        """
        ...

    @abstractmethod
    def break_object(self) -> None:
        """
        Разрушает объект.

        :return: None

        >>> class Stone(PhysicalObject):
        ...     def move(self, distance: float) -> None:
        ...         pass
        ...     def break_object(self) -> None:
        ...         pass
        >>> stone = Stone(5.0, "granite")
        >>> stone.break_object()
        """
        ...


class DigitalService(ABC):
    """
    Абстрактный класс, описывающий цифровой сервис.
    """

    def __init__(self, name: str, users_count: int) -> None:
        """
        :param name: Название сервиса
        :param users_count: Количество пользователей (>= 0)
        """
        if not name:
            raise ValueError("Название сервиса не может быть пустым")
        if users_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным")

        self.name: str = name
        self.users_count: int = users_count

    @abstractmethod
    def register_user(self, user_id: int) -> bool:
        """
        Регистрирует нового пользователя.

        :param user_id: Идентификатор пользователя (должен быть > 0)
        :return: Успешность регистрации

        >>> class SocialNetwork(DigitalService):
        ...     def register_user(self, user_id: int) -> bool:
        ...         return True
        ...     def delete_user(self, user_id: int) -> bool:
        ...         return True
        >>> sn = SocialNetwork("TestNet", 10)
        >>> sn.register_user(1)
        True
        """
        ...

    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        """
        Удаляет пользователя из сервиса.

        :param user_id: Идентификатор пользователя
        :return: Успешность удаления

        >>> class App(DigitalService):
        ...     def register_user(self, user_id: int) -> bool:
        ...         return True
        ...     def delete_user(self, user_id: int) -> bool:
        ...         return True
        >>> app = App("DemoApp", 5)
        >>> app.delete_user(2)
        True
        """
        ...


class Storage(ABC):
    """
    Абстрактный класс, описывающий хранилище данных.
    """

    def __init__(self, capacity: int, used: int) -> None:
        """
        :param capacity: Общая ёмкость хранилища (> 0)
        :param used: Используемый объём (>= 0 и <= capacity)
        """
        if capacity <= 0:
            raise ValueError("Ёмкость должна быть больше 0")
        if used < 0 or used > capacity:
            raise ValueError("Используемый объём некорректен")

        self.capacity: int = capacity
        self.used: int = used

    @abstractmethod
    def write(self, size: int) -> None:
        """
        Записывает данные в хранилище.

        :param size: Размер данных (> 0)
        :return: None

        >>> class Disk(Storage):
        ...     def write(self, size: int) -> None:
        ...         pass
        ...     def clear(self) -> None:
        ...         pass
        >>> disk = Disk(100, 10)
        >>> disk.write(20)
        """
        ...

    @abstractmethod
    def clear(self) -> None:
        """
        Очищает хранилище.

        :return: None

        >>> class Cache(Storage):
        ...     def write(self, size: int) -> None:
        ...         pass
        ...     def clear(self) -> None:
        ...         pass
        >>> cache = Cache(50, 25)
        >>> cache.clear()
        """
        ...


if __name__ == "__main__":
    # Проверка работоспособности документации и примеров
    doctest.testmod()

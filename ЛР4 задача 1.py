from typing import List


class SocialNetwork:
    """
    Базовый класс социальной сети.

    Атрибуты:
        name (str): Название социальной сети.
        audience (int): Количество пользователей.
        _users (List[str]): Список зарегистрированных пользователей (непубличный атрибут).
    """

    def __init__(self, name: str, audience: int) -> None:
        """
        Инициализация социальной сети.

        Args:
            name (str): Название сети.
            audience (int): Количество пользователей.
        """
        self.name: str = name
        self.audience: int = audience
        self._users: List[str] = []  # защищённый атрибут (инкапсуляция)

    def __str__(self) -> str:
        """Возвращает удобочитаемое строковое представление объекта."""
        return f"Социальная сеть {self.name}, пользователей: {self.audience}"

    def __repr__(self) -> str:
        """Возвращает официальное строковое представление объекта."""
        return f"SocialNetwork(name='{self.name}', audience={self.audience})"

    def register_user(self, username: str) -> None:
        """
        Регистрирует нового пользователя.

        Args:
            username (str): Имя пользователя.
        """
        self._users.append(username)
        self.audience += 1

    def post_message(self, username: str, message: str) -> str:
        """
        Публикует сообщение от имени пользователя.

        Args:
            username (str): Имя пользователя.
            message (str): Текст сообщения.

        Returns:
            str: Подтверждение публикации.
        """
        return f"{username} опубликовал сообщение: {message}"


class VK(SocialNetwork):
    """
    Дочерний класс социальной сети VK.

    Дополнительные атрибуты:
        music_service (bool): Наличие музыкального сервиса.
        __internal_id (int): Внутренний идентификатор платформы (приватный атрибут).
    """

    def __init__(self, name: str, audience: int, music_service: bool) -> None:
        """
        Расширенный конструктор VK.

        Args:
            name (str): Название сети.
            audience (int): Количество пользователей.
            music_service (bool): Есть ли музыкальный сервис.
        """
        super().__init__(name, audience)
        self.music_service: bool = music_service
        self.__internal_id: int = 1  # приватный атрибут (полная инкапсуляция)

    def __str__(self) -> str:
        """Расширенное строковое представление VK."""
        return f"VK ({self.name}), пользователей: {self.audience}, музыка: {self.music_service}"

    def __repr__(self) -> str:
        """Официальное представление VK."""
        return f"VK(name='{self.name}', audience={self.audience}, music_service={self.music_service})"

    def post_message(self, username: str, message: str) -> str:
        """
        Переопределённый метод публикации сообщения.

        Причина перегрузки:
        В VK реализована возможность прикрепления музыки к сообщению,
        поэтому формат публикации отличается от базового класса.

        Args:
            username (str): Имя пользователя.
            message (str): Текст сообщения.

        Returns:
            str: Подтверждение публикации с особенностями VK.
        """
        return f"[VK] {username} опубликовал запись: {message} 🎵"

    def play_music(self, track_name: str) -> str:
        """
        Воспроизводит музыкальный трек.

        Args:
            track_name (str): Название трека.

        Returns:
            str: Сообщение о воспроизведении.
        """
        if self.music_service:
            return f"Сейчас играет: {track_name}"
        return "Музыкальный сервис недоступен"


if __name__ == "__main__":
    # Пример использования
    vk = VK("ВКонтакте", 1000000, True)
    vk.register_user("Альберт Авдеев")
    print(vk)
    print(vk.post_message("Альберт Авдеев", "Ответ на ЛР4"))
    print(vk.play_music("Русские народные басни - исполнитель неизвестен"))

import json
import logging

logging.basicConfig(level=logging.INFO)


def open_file(path: str) -> str:
    """Осуществляет чтение из файла 

    Args:
        path(str) - путь к файлу, необходимый для открытия

    Returns:
        str - текстовые данные
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            main = file.read()
        return main
    except Exception as ex:
        logging.error(f"Error opening the file: {ex}\n{ex.args}\n")


def open_file_bytes(path: str) -> str:
    """Осуществляет чтение из файла в бинарном режиме

    Args:
        path(str) - путь к файлу, необходимый для открытия

    Returns:
        str - текстовые данные
    """
    try:
        with open(path, "rb") as file:
            main = file.read()
        return main
    except Exception as ex:
        logging.error(f"Error opening the file: {ex}\n{ex.args}\n")


def open_key_des(path: str) -> bytes:
    """Десериализация ключа симметричного алгоритма

    Args:
        path(str) - путь к файлу, необходимый для открытия

    Returns:
        bytes - данные в байтах
    """
    try:
        with open(path, "rb") as file:
            main = file.read()
        return main
    except Exception as ex:
        logging.error(f"Error opening the file: {ex}\n{ex.args}\n")


def write_text(path: str, data: str) -> None:
    """Осуществляет запись данных в файл 

    Args:
        path(str) - путь к файлу, необходимый для открытия
        data(str) - данные для записи

    Returns:
        None
    """
    try:
        with open(path, "w", encoding="utf-8") as file:
            file.write(data)
    except Exception as ex:
        logging.error(f"Error writing the file: {ex}\n{ex.args}\n")


def write_text_bytes(path: str, data: str) -> None:
    """Осуществляет запись данных в файл в бинарном режиме

    Args:
        path(str) - путь к файлу, необходимый для открытия
        data(str) - данные для записи

    Returns:
        None
    """
    try:
        with open(path, "wb") as file:
            file.write(data)
    except Exception as ex:
        logging.error(f"Error opening the file: {ex}\n{ex.args}\n")


def write_key_ser(path: str, key: bytes) -> None:
    """Сериализация ключа симмеричного алгоритма в файл

    Args:
        path(str) - путь к файлу, необходимый для открытия
        key(bytes) - данные для записи

    Returns:
        None
    """
    try:
        with open(path, "wb") as file:
            file.write(key)
    except Exception as ex:
        logging.error(f"Error writing the file: {ex}\n{ex.args}\n")


def read_json(path: str) -> dict:
    """Осуществляет чтение данных из json-файла

    Args:
        path(str) - путь к файлу, необходимый для открытия

    Returns:
        dict - данные json-файла в виде словаря
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as ex:
        logging.error(f"Error reading the file: {ex}\n{ex.args}\n")

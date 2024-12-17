import os  # python -m pytest
import json
import pytest

from cryptography.hazmat.primitives.asymmetric import rsa

from asymmetric_algortm import asymmetric_key
from key_serialization import private_key_ser, public_key_ser
from symmetric_algortm import symmetric_key
from working_with_a_file import open_file, open_file_bytes, open_key_des, write_text, write_text_bytes, write_key_ser, read_json


@pytest.fixture
def key() -> tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
    """Фикстура для генерации асимметричного ключа"""
    return asymmetric_key()


def test_key(key: tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]):
    """Тестирование функции генерации пары ключей для асимметричного алгоритма шифрования"""
    assert isinstance(key[0], rsa.RSAPublicKey)
    assert isinstance(key[1], rsa.RSAPrivateKey)


def test_open_file(mocker):
    """Тестирование функции чтения из файла"""
    test_data = os.urandom(8)
    file_path = "test_path.txt"
    mock_file = mocker.patch("builtins.open", mocker.mock_open())
    mock_file.return_value.__enter__.return_value.read.return_value = test_data
    result = open_file(file_path)

    mock_file.assert_called_once_with(file_path, "r", encoding="utf-8")
    assert result == test_data


@pytest.mark.parametrize("key_size", [8, 16])
def test_open_file_bytes(mocker, key_size):
    """Тестирование функции чтения из файла в бинарном режиме"""
    test_data = os.urandom(key_size)
    file_path = "test_path.txt"
    mock_file = mocker.patch("builtins.open", mocker.mock_open())
    mock_file.return_value.__enter__.return_value.read.return_value = test_data
    result = open_file_bytes(file_path)

    mock_file.assert_called_once_with(file_path, "rb")
    assert result == test_data


def test_open_key_des(mocker):
    """Тестирование функции десериализации ключа симметричного алгоритма"""
    test_data = os.urandom(8)
    file_path = "test_path.txt"
    mock_file = mocker.patch("builtins.open", mocker.mock_open())
    mock_file.return_value.__enter__.return_value.read.return_value = test_data
    result = open_key_des(file_path)

    mock_file.assert_called_once_with(file_path, "rb")
    assert result == test_data


def test_asymmetric_key_serialization():
    private_key, public_key = asymmetric_key()

    public_key_file = "public.pem"
    private_key_file = "private.pem"

    public_key_ser(public_key_file, public_key)
    private_key_ser(private_key_file, private_key)

    assert os.path.exists(public_key_file)
    assert os.path.exists(private_key_file)

    os.remove(public_key_file)
    os.remove(private_key_file)


@pytest.mark.parametrize("key_size", [8, 16, 24])
def test_symmetric_key_serialization(key_size):
    key = symmetric_key(key_size)

    file = "symmetric_key.txt"
    write_key_ser(file, key)
    data = open_key_des(file)

    assert data == key
    os.remove(file)


@pytest.mark.parametrize("key_size", [8, 16])
def test_write_text(mocker, key_size):
    """Тестирование функции записи данных в файл"""
    test_data = os.urandom(key_size)
    file_path = "test_path.txt"
    mock_file = mocker.mock_open()
    mocker.patch("builtins.open", mock_file)
    write_text(file_path, test_data)

    mock_file.assert_called_once_with(file_path, "w", encoding="utf-8")
    mock_file().write.assert_called_once_with(test_data)


def test_write_text_bytes(mocker):
    """Тестирование функции записи данных в файл в бинарном режиме"""
    test_data = os.urandom(8)
    file_path = "test_path.txt"
    mock_file = mocker.mock_open()
    mocker.patch("builtins.open", mock_file)
    write_text_bytes(file_path, test_data)

    mock_file.assert_called_once_with(file_path, "wb")
    mock_file().write.assert_called_once_with(test_data)


@pytest.mark.parametrize("key_size", [8, 16])
def test_write_key_ser(mocker, key_size):
    """Тестирование функции сериализации ключа симмеричного алгоритма в файл"""
    test_data = os.urandom(key_size)
    file_path = "test_path.txt"
    mock_file = mocker.patch("builtins.open", mocker.mock_open())
    write_key_ser(file_path, test_data)

    mock_file.assert_called_once_with(file_path, "wb")
    mock_file().write.assert_called_once_with(test_data)


@pytest.fixture
def key(key_size) -> bytes:
    """Фикстура для генерации симметричного ключа"""
    return symmetric_key(key_size)


@pytest.mark.parametrize("key_size", [8, 16, 24])
def test_key(key, key_size):
    """Тестирование функции генерации пары ключей для симметричного алгоритма шифрования"""
    assert len(key) == key_size, "Симметричный ключ должен иметь размер 8 байт"
    assert isinstance(key, bytes), "Симметричный ключ должен иметь тип байт"


@pytest.mark.parametrize("mock_data, expected_result", [
    ('{"animal": "cat", "bird": "stork"}', {
        "animal": "cat",
        "bird": "stork"
    }),
    ('{"name": "Badger", "breed": "Maine Coon", "floor": "the male", "years": []}',
     {
         "name": "Badger",
         "breed": "Maine Coon",
         "floor": "the male",
         "years": []
     }),
    ('{}', {}),
])
def test_read_json(mocker, mock_data, expected_result):
    """Тестирование функции чтения данных из json-файла"""
    mock_json = mocker.patch("json.load")
    mock_json.return_value = json.loads(mock_data)
    file_path = "test_path.json"
    mock_file = mocker.patch("builtins.open", mocker.mock_open())
    result = read_json(file_path)

    mock_file.assert_called_once_with(file_path, "r", encoding="utf-8")
    mock_json.assert_called_once_with(mock_file())
    assert result == expected_result

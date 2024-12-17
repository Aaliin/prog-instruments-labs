import base64
import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import asymmetric, hashes, padding 
from cryptography.hazmat.primitives.asymmetric import rsa

from working_with_a_file import open_file, open_key_des, open_file_bytes, write_text, write_text_bytes


def symmetric_key(byte_count: int) -> bytes:
    """Генерация ключа симметричного алгоритма шифрования
    
    Args:
        byte_count(int) - количество байт 

    Returns:
        bytes - сгенерированный симметричный ключ
    """
    return os.urandom(byte_count)


def symmetric_encryption(key: rsa.RSAPublicKey, symmetric_key: bytes) -> bytes:
    """Осуществляет шифрование и паддинг текста симметричным алгоритмом

    Args:
        key(rsa.RSAPublicKey) - публичный ключ
        symmetric_key(dytes) - симметричный ключ
        
    Returns:
        bytes - зашифрованный текст
    """
    data = key.encrypt(
                symmetric_key,
                asymmetric.padding.OAEP(
                    mgf=asymmetric.padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
                )
    return data


def symmetric_decryption(key: rsa.RSAPublicKey, symmetric_key: bytes) -> str:
    """Осуществляет дешифрование и депаддинг текста симметричным алгоритмом

    Args:
        key(rsa.RSAPublicKey) - публичный ключ
        symmetric_key(dytes) - симметричный ключ
        
    Returns:
        bytes - дэшифрованный текст
    """
    data = key.decrypt(
                symmetric_key,
                asymmetric.padding.OAEP(
                    mgf=asymmetric.padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )
    return data


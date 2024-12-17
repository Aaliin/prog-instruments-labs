from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa

from key_deserialization import private_key_des, public_key_des
from working_with_a_file import open_key_des, write_key_ser, write_text_bytes


def asymmetric_key() -> tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
    """Генерация пары ключей для асимметричного алгоритма шифрования

    Returns:
        tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey] - кортеж с сгенерированным открытым и закрытым ключам
    """
    keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    private_key = keys
    public_key = keys.public_key()
    return public_key, private_key


def asymmetric_encryption(path_initial_key: str, public: str) -> bytes:
    """Осуществляет шифрование и паддинг текста асимметричным алгоритмом

    Args:
        path_initial_key(str) - путь к файлу с исходным симметричным ключом
        public(str) - путь к файлу с public ключом
        path_save(str) - путь к файлу для сохранения зашифрованного симметричного ключа 
        
    Returns:
        None
    """
    text = open_key_des(path_initial_key)
    public_key = public_key_des(public)
    encripted_text = public_key.encrypt(
        text,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                     algorithm=hashes.SHA256(),
                     label=None))
    #write_text_bytes(path_save, encripted_text)
    return encripted_text


def asymmetric_decryption(path_save: str, private: str) -> bytes:
    """Осуществляет дешифрование и депаддинг текста асимметричным алгоритмом

    Args:
        path_save(str) - путь к файлу с сохраненным зашифрованным симметричным ключом
        private(str) - путь к файлу с private ключом
        path_decryption(str) - путь к файлу с дешифрованным симметричным ключом
        
    Returns:
        bytes - дешифрованный текст
    """
    text = open_key_des(path_save)
    private_key = private_key_des(private)
    decripted_text = private_key.decrypt(
        text,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                     algorithm=hashes.SHA256(),
                     label=None))
    #write_key_ser(path_decryption, decripted_text)
    return decripted_text

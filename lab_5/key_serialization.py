import logging

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

logging.basicConfig(level=logging.INFO)


def public_key_ser(public_pem: str, public_key: rsa.RSAPublicKey) -> None:
    """Осуществляет сериализацию открытого ключа в файл

    Args:
        public_pem(str) - путь к файлу, в который пойдет запись 
        public_key(rsa.RSAPublicKey) - открытый rsa ключ
        
    Returns:
        None
    """
    try:
        with open(public_pem, 'wb') as public_out:
            public_out.write(
                public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo))
    except Exception as ex:
        logging.error(f"Error writing the file: {ex}\n{ex.args}\n")


def private_key_ser(private_pem: str, private_key: rsa.RSAPrivateKey) -> None:
    """Осуществляет сериализацию закрытого ключа в файл

    Args:
        public_pem(str) - путь к файлу, в который пойдет запись 
        private_key(rsa.RSAPrivateKey) - закрытый rsa ключ
        
    Returns:
        None
    """
    try:
        with open(private_pem, 'wb') as private_out:
            private_out.write(
                private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()))
    except Exception as ex:
        logging.error(f"Error writing the file: {ex}\n{ex.args}\n")

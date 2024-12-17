import logging

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

logging.basicConfig(level=logging.INFO)


def public_key_des(public_pem: str) -> rsa.RSAPublicKey:
    """Осуществляет десериализацию открытого ключа в файл
    
    Args:
        public_pem(str) - путь к файлу, в который пойдет запись  
        
    Returns:
        rsa.RSAPublicKey - открытый ключ
    """
    try:
        with open(public_pem, 'rb') as pem_in:
            public_bytes = pem_in.read()
        d_public_key = serialization.load_pem_public_key(public_bytes)
        return d_public_key
    except Exception as ex:
        logging.error(f"Error writing the file: {ex}\n{ex.args}\n")


def private_key_des(private_pem: str) -> rsa.RSAPrivateKey:
    """Осуществляет десериализацию закрытого ключа в файл

    Args:
        private_pem(str) - путь к файлу, в который пойдет запись  
        
    Returns:
        rsa.RSAPrivateKey - приватный ключ 
    """
    try:
        with open(private_pem, 'rb') as pem_in:
            private_bytes = pem_in.read()
        d_private_key = serialization.load_pem_private_key(
            private_bytes,
            password=None,
        )
        return d_private_key
    except Exception as ex:
        logging.error(f"Error writing the file: {ex}\n{ex.args}\n")

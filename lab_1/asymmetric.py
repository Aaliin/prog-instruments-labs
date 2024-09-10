from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa


class Asymmetric:
    """Class for asymmetric encryption operations."""
    
    def __init__(self) -> None:
        """Initializes the private and public keys to None."""
        self.private_key = None
        self.public_key = None

    def generate_key_pair(self) -> tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
        """
        Generates an asymmetric key pair and serializes them to files. 

        Returns:
            tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]: tuple with generated public and private keys
        """
        keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.private_key = keys
        self.public_key = keys.public_key()
        return (self.private_key, self.public_key)

    def process_symmetric_key(self, key: bytes, key_path: str, operation: str) -> bytes:
        """
        Processes a symmetric key using asymmetric encryption.

        Args:
            key (bytes): The symmetric key to process.
            key_path (str): The path to the asymmetric key.
            operation (str): The operation to perform ('encrypt' or 'decrypt').

        Returns:
            bytes: The processed key.
        """
        if operation == "encrypt":
            public_key = self.deserialize_key(key_path, "public")
            return public_key.encrypt(key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                        algorithm=hashes.SHA256(), label=None))
        elif operation == "decrypt":
            private_key = self.deserialize_key(key_path, "private")
            return private_key.decrypt(key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                          algorithm=hashes.SHA256(), label=None))
        else:
            raise ValueError("Invalid mode provided. Use 'encrypt' or 'decrypt'.")

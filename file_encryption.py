import base64
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


# Converting a user-friendly password into a Fernet-compatible key
def password_to_fernet_key(password: str, salt: bytes = b'static_salt_123') -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


def encrypt_file(file_data, key):
    try:
        fernet = Fernet(key)
        return fernet.encrypt(file_data)
    except Exception as e:
        raise ValueError("Encryption failed: " + str(e))


def decrypt_file(file_data, key):
    try:
        fernet = Fernet(key)
        return fernet.decrypt(file_data)
    except InvalidToken:
        raise ValueError("Decryption failed: Invalid password or corrupted file")

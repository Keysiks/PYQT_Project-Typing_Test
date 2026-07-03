import hashlib
import secrets


def hash_password(password: str, salt: bytes = None) -> tuple[str, bytes]:
    """Hash password with salt using PBKDF2."""
    if salt is None:
        salt = secrets.token_bytes(16)
    hash_bytes = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return hash_bytes.hex(), salt


def verify_password(password: str, hashed: str, salt: bytes) -> bool:
    """Verify password against hash and salt."""
    new_hash, _ = hash_password(password, salt)
    return secrets.compare_digest(new_hash, hashed)
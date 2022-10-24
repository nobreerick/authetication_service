import re
import hashlib

class ControllerUser:
    @classmethod
    def validate_username(cls, username: str) -> bool:
        # Username requirements:
        # any alphanumeric;
        # None special character;
        # minimun 8, maximun 20 password lenght.
        REGEX = r"^[\w+(?!\W)]{8,20}$"
        if re.search(REGEX, username): return True
        else: return False

    @classmethod
    def validate_password(cls, password: str) -> bool:
        # Password requirements:
        # at least one uppercase letter;
        # at least one lowercase letter;
        # at least one digit;
        # at least one special character;
        # minimun 8 password lenght;
        REGEX = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if re.match(REGEX, password): return True
        else: return False
    
    @classmethod
    def encrypt(cls, password: str) -> str:
        result = hashlib.md5(password.encode())
        result_hex = result.hexdigest()
        return result_hex

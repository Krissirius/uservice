from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from core.config import SECRET_KEY

# Секретный ключ и настройки JWT
 # Замените на свой секретный ключ из .env
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Настройка для хеширования паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Функция хеширования пароля
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Функция проверки пароля
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Функция для создания JWT токена
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
"""Password hashing and JWT helpers."""

import os
from datetime import datetime, timedelta
from typing import Optional

from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY = os.environ.get("TEMPUS_SECRET_KEY", "dev-only-change-me")
ALGORITHM = "HS256"
TOKEN_TTL_MINUTES = int(os.environ.get("TEMPUS_TOKEN_TTL_MINUTES", "720"))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def create_access_token(subject: str, expires_minutes: Optional[int] = None) -> str:
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes or TOKEN_TTL_MINUTES)
    payload = {"sub": subject, "exp": expire, "iat": datetime.utcnow()}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> dict:
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])


def token_subject(token: str) -> Optional[str]:
    try:
        return decode_token(token).get("sub")
    except JWTError:
        return None

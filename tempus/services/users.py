from typing import Optional

from sqlalchemy.orm import Session

from ..db.models import User


def get_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email.lower()).one_or_none()


def create_user(db: Session, email: str, password_hash: str, display_name: str = "") -> User:
    user = User(email=email.lower(), password_hash=password_hash, display_name=display_name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

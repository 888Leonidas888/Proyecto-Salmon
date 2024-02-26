"""Clase para definir usuarios."""

from models.base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from passlib.hash import sha256_crypt


class User(Base):
    """Define clase usuario."""
    __tablename__ = "users"
    id_user: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(String(30), nullable=False)
    password_hash: Mapped[str] = mapped_column(String(30), nullable=False)
    condition: Mapped[str]=mapped_column(String(20), default='operador')

    def __repr__(self) -> str:
        """Este método especial regresa un representación
            de la clase User.
        """
        return f'User(id_user={self.id_user}, username={self.username})'

    def __init__(self, id_user: int, username: str, password: str) -> None:
        """
        Inicializa una nueva instancia de la clase User.

        Args:
            id_user (int): Número único que idenfica al usuario.
            username (str): Nombre de usuario.
            password (str): Contraseña del usuario.
        """
        self.id_user = id_user
        self.username = username
        self.password_hash = self._hash_password(password)

    def _hash_password(self, password: str) -> str:
        """
        Aplica un hash seguro a la contraseña del usuario.

        Args:
            password (str): Contraseña del usuario.

        Returns:
            str: Contraseña hasheada.
        """
        return sha256_crypt.hash(password)

    def verify_password(self, password: str) -> bool:
        """
        Verifica si una contraseña proporcionada coincide con la contraseña del usuario.

        Args:
            password (str). Conraseña a verificar.

        Returns:
            bool: True si la contraseña coincide.False caso contrario.
        """
        return sha256_crypt.verify(password, self.password_hash)

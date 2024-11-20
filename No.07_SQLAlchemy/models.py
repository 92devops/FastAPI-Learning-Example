from   database import  Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text


class User(Base):
    __tablename__  = "t_user"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(32), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    email = Column(String(64), nullable=False, unique=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))



from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class user(connector.Manager.Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('book_id_seq'), primary_key=True)
    correo = Column(String(50))
    password = Column(String(12))
    name = Column(String(20))
    last_name= Column(String(30))


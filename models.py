from enum import unique
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher (Base):
    __tablename__ = 'publisher'
    
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column (sq.String (length=40), unique = True)
    
class Book(Base):
    __tablename__ = "book"
    

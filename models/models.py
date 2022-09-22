from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher (Base):
    __tablename__ = 'publisher'
    
    id = Column(Integer, primary_key=True)
    name = Column (String (length=40), unique = True)
    
    def __str__(self):
        return f'{self.id}: {self.name}'
    
class Book(Base):
    __tablename__ = "book"
    
    id = Column(Integer, primary_key=True)
    id_publisher =  Column(Integer, ForeignKey('publisher.id'), nullable=False)
    title = Column (String (length=40), unique = True)
    
    con_pub = relationship(Publisher, backref = 'con_book')
    
class Shop(Base):
    __tablename__ = 'shop'
    
    id = Column(Integer, primary_key=True)
    name = Column (String (length=40), unique = True)
    
class Stock(Base):
    __tablename__ = 'stock'
    
    id = Column(Integer, primary_key=True)
    id_book =  Column(Integer, ForeignKey('book.id'), nullable=False)
    id_shop =  Column(Integer, ForeignKey('shop.id'), nullable=False)
    count = Column (Integer)
    
    con_book = relationship(Book, backref = 'con_stock')
    con_shop = relationship(Shop, backref = 'con_stock')
    
class Sale(Base):
    __tablename__ = 'sale'
    
    id = Column(Integer, primary_key=True)
    id_stock =  Column(Integer, ForeignKey('stock.id'), nullable=False)
    price = Column(Float, nullable=False)
    date_sale = Column (Date, nullable=False)
    count = Column (Integer)
    
    con_stock = relationship(Stock, backref = 'con_sale')
    
def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
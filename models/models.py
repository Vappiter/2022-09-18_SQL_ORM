import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher (Base):
    __tablename__ = 'publisher'
    
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column (sq.String (length=40), unique = True)
    
    def __str__(self):
        return f'{self.id}: {self.name}'
    
class Book(Base):
    __tablename__ = "book"
    
    id = sq.Column(sq.Integer, primary_key=True)
    id_publisher = sq. Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)
    title = sq.Column (sq.String (length=40), unique = True)
    
    con_pub = relationship(Publisher, backref = 'con_book')
    
class Shop(Base):
    __tablename__ = 'shop'
    
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column (sq.String (length=40), unique = True)
    
class Stock(Base):
    __tablename__ = 'stock'
    
    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq. Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq. Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    count = sq.Column (sq.Integer)
    
    con_book = relationship(Book, backref = 'con_stock')
    con_shop = relationship(Shop, backref = 'con_stock')
    
class Sale(Base):
    __tablename__ = 'sale'
    
    id = sq.Column(sq.Integer, primary_key=True)
    id_stock = sq. Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column (sq.Date, nullable=False)
    count = sq.Column (sq.Integer)
    
    con_stock = relationship(Stock, backref = 'con_sale')
    
def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
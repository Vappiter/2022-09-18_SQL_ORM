import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models.models import create_tables, Publisher, Book, Shop, Stook, Sale

DSN = 'postgresql://postgres:123456@localhost:5432/PythonSQL'

if __name__ == '__main__':
    
 engine = sqlalchemy.create_engine(DSN)
 
 create_tables(engine)
 
 Session = sessionmaker(bind=engine)
 session = Session()
 
 
 
 session.close()
 
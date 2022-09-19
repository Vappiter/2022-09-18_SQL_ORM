from turtle import title
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models.models import create_tables, Publisher, Book, Shop, Stock, Sale
import json
import os

DSN = 'postgresql://postgres:123456@localhost:5432/PythonSQL'

if __name__ == '__main__':
 
 file_path = (os.path.split(__file__)) # Считывает текущую директорию скрипта, тут же должны храниться файлы токенов
 os.chdir(file_path [0]) # Устанавливает директорию
 with open ('test_data.json',encoding='utf-8') as file_read:
    data_json = json.load(file_read) 
        
 engine = sqlalchemy.create_engine(DSN)
 
 create_tables(engine)
 
 Session = sessionmaker(bind=engine)
 session = Session()
 
#  Input data from json file
 
 for var1 in data_json:
     if var1 ['model'] == 'publisher':
      var_pub = Publisher (name = var1['fields']['name'])   
      session.add(var_pub)
      session.commit()
     elif var1 ['model'] == 'book':
         var_book = Book (title = var1['fields']['title'], id_publisher = var1['fields']['id_publisher'])
         session.add(var_book)
         session.commit() 
     elif var1 ['model'] == 'shop':
         var_shop = Shop (name = var1['fields']['name'])
         session.add(var_shop)
         session.commit()
     elif var1 ['model'] == 'stock':
         var_stock = Stock (id_book = var1['fields']['id_book'],id_shop = var1['fields']['id_shop'], count = var1['fields']['count'])
         session.add(var_stock)
         session.commit()    
     elif var1 ['model'] == 'sale':
         var_sale = Stock (id_stock = var1['fields']['id_stock'],price = var1['fields']['price'],date_sale = var1['fields']['date_sale'], count = var1['fields']['count'])
         session.add(var_sale)
         session.commit()
     
    #  Output publisher
    
 q = session.query (Publisher)
 for s in q.all():
   print (s.id, s.name)
        
    # Output book
        
 q = session.query (Book)
 for s in q.all():
   print (s.id, s.title, s.id_publisher)
 session.close()
 
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models.models import create_tables, Publisher, Book, Shop, Stock, Sale
import json
import os

type_bd = 'postgresql'
username_bd = 'postgres'
password_bd = '123456'
comp_bd = 'localhost'
port_bd = '5432'
name_bd = 'PythonSQL'

var_connect_bd = type_bd + '://' + username_bd + ':' + password_bd + '@' + comp_bd + ':' + port_bd + '/' + name_bd

# DSN = 'postgresql://postgres:123456@localhost:5432/PythonSQL'

if __name__ == '__main__':
 
 file_path = (os.path.split(__file__)) # Считывает текущую директорию скрипта, тут же должны храниться файлы токенов
 os.chdir(file_path [0]) # Устанавливает директорию
 with open ('test_data.json',encoding='utf-8') as file_read:
    data_json = json.load(file_read) 
        
 engine = sqlalchemy.create_engine(var_connect_bd)
 
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
         var_sale = Sale (id_stock = var1['fields']['id_stock'],price = var1['fields']['price'],date_sale = var1['fields']['date_sale'], count = var1['fields']['count'])
         session.add(var_sale)
         session.commit()
     
    #  Output publisher
 
 print (f"\n Издатели \n")   
 q = session.query (Publisher)
 for s in q.all():
   print (s.id, s.name)
        
    # Output book
    
 print (f"\n Книги и кто их издает \n")
 q = session.query(Publisher).join(Book.con_pub)
 for s in q.all():
   print (f'Издатель: {s.name}\n')
   print(f'Издаваемые им книги: \n')
   for s1 in s.con_book:
     print (s1.title)  
   print(f'\n')  
   
 print (f'Введите ID издателя, чтоб узнать какие книги он выпускает:')  
 q = session.query (Publisher)
 for s in q.all():
   print (s.id, s.name)
 var_id_pub = int(input())
 q = session.query(Publisher).join(Book.con_pub).filter(Publisher.id == var_id_pub)
 for s in q.all():
   print (f'Издатель: {s.name}\n')
   print(f'Издаваемые им книги:')
   for s1 in s.con_book:
     print (s1.title)  
   print(f'\n')   

 pub_list ={}
 q = session.query(Shop.name, Publisher.name).join(Shop.con_stock).join(Stock.con_book).join(Book.con_pub)
#  pub_list = {s[1]: s[0] 
 for s in q.all():
   name_shop, name_pub = s
   if name_pub not in pub_list.keys():
    var_list = {name_pub:name_shop}
    pub_list.update(var_list)
   else:
    if name_shop not in pub_list[name_pub]:
     pub_list[name_pub] = pub_list[name_pub] + ', ' + name_shop
    
 print (pub_list) 

 session.close()
 
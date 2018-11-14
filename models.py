from peewee import (CharField,
                    SqliteDatabase,
                    Model,
                    TextField,
                    IntegerField,
                    OperationalError,
                    IntegrityError,
                    DateTimeField )
import datetime
db = SqliteDatabase("statements.db")
statements = [
    {'id':1,'amount': 1000,'action': 'deposit', 'balance': 2000},
    {'id': 2,'amount': 1000,'action': 'deposit', 'balance': 2000}
      
]
customers = [
    {'id':1,'customer_name': 'felicious'},
    {'id': 2,'customer_name': 'felicious'}
    
    
    
]



class Statement(Model):
    
    date=DateTimeField(default=datetime.datetime.now)
    amount=IntegerField(default=100000000)
    action = CharField(max_length=100)
    balance = IntegerField(default=100000000)    

    class Meta:
        database = db



class Customer(Model):
    
    
    customer_name = CharField(max_length=200)
   
    

    class Meta:
        database = db

def initialize():
    return None
    try:
        Statement.create_table()
    except OperationalError:
        pass
    for statement in statements:
        try:
            Statement.create(
                date=datetime.datetime.now(),
                amount=statement.get('amount'),
                action=statement.get('action'),
                balance=statement.get('balance'),
                
               
                )
        except IntegrityError:
            pass


    try:
            Customer.create_table()
    except OperationalError:
            pass
    for customer in customers:
        try:
            Customer.create(
                    customer_name=customer.get('customer_name'),
                   
                    )
        except IntegrityError:
            pass
    
    



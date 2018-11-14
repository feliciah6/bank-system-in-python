from flask import (Flask,
                    render_template,
                   request,
                   make_response,
                   redirect,
                   jsonify
                    )
import datetime
import json
import models
from models  import Statement
from models import Customer 
 
app = Flask('app')
@app.route('/')
def index():
    models.initialize()
    return render_template("index.html")





@app.route('/transact', methods=['POST', 'GET'])
def register():

    data = dict(request.form.items())
    if data.get('email', None):
        Statement.create(
            customer_name=data.get('customer_name'),
            amount=data.get('amount'),
            action=data.get('action'),
           
            
            
        )
    return render_template("cashier.html")


@app.route('/transact/save', methods=['POST'])
def transactions():
    data = dict(request.form.items())
    query = Customer.select().where(Customer.customer_name == 'lauren')
    if query.exists():
      return query.get().id 

    return jsonify(data)
    Customer.create(
        customer_name=data.get('customer_name'),
       
        )

    return jsonify(data)


@app.route('/transaction', methods=['POST','GET'])
def customers():
  models.initialize()
  customers = Customer.select()
  query = Customer.select().where(Customer.customer_name == 'lauren')
    if query.exists():
      return query.get().id 

  
  return render_template('transactions.html',customers=customers)

  # models.initialize()
  # data = dict(request.form.items())
  # if data.get('customer_name', None):
  #   Customer.create(
  #     Customer_name=data.get('customer_name','felicious'),
  #   )
  #   return "success"
    # return render_template("transactions.html", customers=customers)

@app.route('/statements')
def see_statements():
    models.initialize()
    query = Statement.select().where(Statement.action == 'deposit')
    if query.exists():
      return query.get().'set balance to zero' 
    else  query.exists():
      return query.get().'set balance to zero' 
    statements = models.Statement.select()
    return render_template("statement.html", statements=statements)
app.run(debug=True, host='0.0.0.0', port=8080)
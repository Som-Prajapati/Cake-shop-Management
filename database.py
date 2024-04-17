import pymongo
customer_id = 0
cake_id = 0


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
    
    # all tables
mycustomer = mydb["customers"]
mycake = mydb["cakes"]
myorder = mydb["orders"]
myprofit = mydb["profit"]

def insert_customer(name,age,gender,address,phone,email):
    mydict = { 'id' :  create_customer_id() ,
            'name' : name ,
            'age' : age ,
            'gender' : gender ,
            'address' : address ,
            'phone' : phone ,
            'email' : email }

    x = mycustomer.insert_one(mydict)  

def insert_cake(name,egg,description,weight,quantity,price):
    mydict = { 'id' :  create_cake_id() ,
            'name' : name ,
            'egg' : egg ,
            'description' : description ,
            'weight' : weight ,
            'quantity' : quantity ,
            'price' : price }

    x = mycake.insert_one(mydict)  

def insert_order(cake_id,cake_name,customer_name,customer_phone,cake_weight,quantity,total):
    mydict = { 'cake_id' :  cake_id ,
            'cake_name' : cake_name ,
            'customer_name' : customer_name ,
            'customer_phone' : customer_phone ,
            'weight' : cake_weight ,
            'quantity' : quantity ,
            'total' : total}

    x = myorder.insert_one(mydict) 

# def insert_profit():

def fetch_customer():
    print('excecuted')
    outer_list = []
    for x in mycustomer.find():
        inner_list = []
        inner_list.append(x['id'])
        inner_list.append(x['name'])
        inner_list.append(x['age'])
        inner_list.append(x['gender'])
        inner_list.append(x['address'])
        inner_list.append(x['phone'])
        inner_list.append(x['email'])
        outer_list.append(inner_list)
    print(outer_list)
    return outer_list

def fetch_cake():
    print('excecuted')
    outer_list = []
    for x in mycake.find():
        inner_list = []
        inner_list.append(x['id'])
        inner_list.append(x['name'])
        inner_list.append(x['egg'])
        inner_list.append(x['description'])
        inner_list.append(x['weight'])
        inner_list.append(x['quantity'])
        inner_list.append(x['price'])
        outer_list.append(inner_list)
    print(outer_list)
    return outer_list

def fetch_order():
    print('excecuted')
    outer_list = []
    for x in myorder.find():
        inner_list = []
        inner_list.append(x['cake_id'])
        inner_list.append(x['cake_name'])
        inner_list.append(x['customer_name'])
        inner_list.append(x['customer_phone'])
        inner_list.append(x['weight'])
        inner_list.append(x['quantity'])
        inner_list.append(x['total'])
        outer_list.append(inner_list)
    print(outer_list)
    return outer_list
    

# def fetch_profit():

def create_customer_id():
    global customer_id
    customer_id += 1
    return customer_id

def create_cake_id():
    global cake_id
    cake_id += 1
    return cake_id

def get_count_customer():
    count = mycustomer.count_documents({})
    print(count)
    return count


from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:@127.0.0.1:3307/ecomm")
connection = engine.connect()
print("Connection successful!")
connection.close()
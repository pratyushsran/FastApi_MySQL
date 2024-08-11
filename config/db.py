from sqlalchemy import create_engine, MetaData
hostname="localhost"
username="root"
password="##"
port=3306
database="notes_db"

engine = create_engine('mysql+pymysql://'+username+':'+password+'@'+hostname+':'+str(port)+'/'+database) 
meta = MetaData()

conn = engine.connect()

from models.index import users

meta.create_all(engine)  

conn = engine.connect()
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData, text
from dotenv import load_dotenv
import os

load_dotenv()
db_username = os.getenv('DB_USERNAME')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
db_password = os.getenv('DB_PASSWORD')
engine = create_engine(f'mysql+pymysql://{db_username}:{db_password}@{db_host}:3306/{db_name}')
sessionlocal = sessionmaker(engine)
if __name__ == "__main__":
  with sessionlocal() as session:
      result = session.execute(text('show tables'))
      instance = result.fetchall()
      print(instance)

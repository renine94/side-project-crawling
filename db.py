from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Base


# 데이터베이스 연결 정보
user = 'root'
password = '0000'
host = 'localhost'
port = '3306'
database = 'crawl_db2'

# SQLAlchemy 엔진 생성
engine = create_engine(f'mysql://{user}:{password}@{host}:{port}/{database}')

# Table 생성 (python mange.py migrate)
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

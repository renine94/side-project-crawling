from sqlalchemy import Column, Integer, String, Boolean, DateTime, create_engine
from sqlalchemy.orm import declarative_base

# 테이블 클래스 생성
Base = declarative_base()


class Board(Base):
    __tablename__ = 'board'

    id = Column(Integer, primary_key=True)
    no = Column(Integer, unique=True)
    content = Column(String(255))
    is_use = Column(Boolean, default=False)

    def __repr__(self):
        return f'<CrawlData no={self.no} content="{self.content}" is_use={self.is_use}>'


class Symbol(Base):
    __tablename__ = 'symbol'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    is_warning = Column(Boolean, default=False)
    updated_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f'<Symbol name="{self.name}" is_warning={self.is_warning} updated_at={self.updated_at}>'


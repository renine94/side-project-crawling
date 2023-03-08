from sqlalchemy import Column, Integer, String, Boolean, DateTime, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

# 테이블 클래스 생성
Base = declarative_base()


class CrawlBoard(Base):
    __tablename__ = 'crawl_board'

    id = Column(Integer, primary_key=True, comment='빗썸 게시글 번호')
    content = Column(String(255), comment='빗썸 게시글 내용')
    is_use = Column(Boolean, default=False, comment='데이터 사용여부')

    def __repr__(self):
        return f'<CrawlData no={self.id} content="{self.content}" is_use={self.is_use}>'


class CrawlSymbol(Base):
    __tablename__ = 'crawl_symbol'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, comment='심볼 이름')
    is_warning = Column(Boolean, default=False, comment='유의 여부')
    new_at = Column(DateTime(timezone=True), default=None, nullable=True)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), comment='업데이트 시간')


    def __repr__(self):
        return f'<Symbol name="{self.name}" is_warning={self.is_warning} updated_at={self.updated_at}>'


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

    idx = Column(Integer, primary_key=True)
    exchange = Column(String(255), comment='거래소')
    market = Column(String(255), unique=True, comment='마켓 종류')
    symbol = Column(String(255), unique=True, comment='코인 심볼')
    caution = Column(Boolean, default=False, comment='유의종목 여부')
    new_listing = Column(Boolean, default=False, comment='신규상장 여부')
    cs_time = Column(DateTime(timezone=True), default=None, nullable=True, comment='유의종목 시작일')
    listing_time = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), comment='상장일')


    def __repr__(self):
        return f'<Symbol name="{self.name}" is_warning={self.is_warning} updated_at={self.updated_at}>'


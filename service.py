from util import save_board_data_from_bithumb, parsing_data
from model import CrawlBoard, CrawlSymbol
from db import get_engine, get_session, create_table


# DB 설정
engine = get_engine()
create_table(engine)
session = get_session(engine)

# 데이터 적재
is_success = save_board_data_from_bithumb()

# 데이터 읽기
boards = session.query(CrawlBoard).order_by(CrawlBoard.id.asc()).all()
for board in boards:
    symbols = parsing_data(board.content)

    if board.id == 3:
        break

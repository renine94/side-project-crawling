from util import save_board_data_from_bithumb, parsing_data
from model import Board
from db import session


save_board_data_from_bithumb()

# 데이터 읽기
boards = session.query(Board).order_by(Board.no.asc()).all()
for board in boards:
    print(board.id)
    print(board.no)
    print(board.content)
    print(board.is_use)

    result = parsing_data(board.content)
    print(result)
    break

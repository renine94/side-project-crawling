from bs4 import BeautifulSoup
import requests
import re

from model import CrawlBoard
from db import get_session, get_engine


def save_board_data_from_bithumb(page: int = 1) -> bool:
    """
    page = 1 (default: 첫페이지)
    크롤링후 Board 테이블에 데이터를 저장
    """
    session = get_session(get_engine())

    try:
        url = f"https://cafe.bithumb.com/view/boards/43?pageNumber={page - 1}&noticeCategory=5"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)
    except Exception as e:
        print(f'URL 요청중 에러 발생: {e}')
        return False

    soup = BeautifulSoup(response.content, 'html.parser')

    ids_tag = soup.select(
        '#dataTables > tbody > tr > td.invisible-mobile.small-size')
    ids = [id_tag.text for id_tag in ids_tag]

    contents_tags = soup.select('#dataTables > tbody > tr > td.one-line > a')
    contents = [content_tag.text for content_tag in contents_tags]

    if len(contents) == 11:
        raise ValueError('존재하지 않는 페이지 입니다.')

    for _id, content in zip(ids, contents):
        if _id.isnumeric() and session.query(CrawlBoard).filter(CrawlBoard.id == _id).count() == 0:
            session.add(CrawlBoard(id=_id, content=content))
    session.commit()
    session.close()
    return True


def parsing_data(content):
    pattern = r'\((\w+)\)'
    return re.findall(pattern, content)

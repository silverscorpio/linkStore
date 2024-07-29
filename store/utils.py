from linkStore.settings import HEADERS
from bs4 import BeautifulSoup
import httpx


def get_link_title(url: str) -> str:
    """Returns the title of the link after parsing the HTML (if found)"""
    r = httpx.get(url, headers=HEADERS)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, features="html.parser")
        if soup.title:
            return str(soup.title.string)
    return ""

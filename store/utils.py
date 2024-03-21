from bs4 import BeautifulSoup
import httpx


def get_link_title(url: str) -> str:
    r = httpx.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, features="html.parser")
        if soup.title:
            return str(soup.title.string)
    return ""

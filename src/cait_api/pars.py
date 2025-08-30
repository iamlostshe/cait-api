"""Модуль парсинга."""

from __future__ import annotations

from aiohttp import ClientSession
from lxml import etree

from cait_api.exceptions import NoDataForThisDayError, UnknownError
from cait_api.types import CAIT

BASE_URL = "https://разговорыоважном.рф"


class CAITParser:
    """Класс парсера."""

    async def init(self) -> None:
        """Инициализация парсера."""
        self.session = ClientSession()
        self.htmlparser = etree.HTMLParser()

    async def get_info(self, date: str) -> CAIT:
        """Информация о товаре."""
        async with self.session.get(f"{BASE_URL}/{date}") as r:
            if r.status == 404:
                raise NoDataForThisDayError

            if r.status != 200:
                raise UnknownError(r.status_code)

            tree = etree.HTML(await r.text(), self.htmlparser)

        urls = {
            i if "http" in i else f"{BASE_URL}{i}"
            for i in tree.xpath("//@href")
            if date in i
        }

        plakat_url = f"{BASE_URL}/{date}/plakat.jpg"
        if plakat_url not in urls:
            plakat_url = None

        return CAIT(
            title=tree.xpath("/html/body/main/section[1]/div[1]/h1")[0].text,
            date=tree.xpath("/html/body/main/section[1]/div[1]/p[1]")[0].text,
            image_url=tree.xpath("/html/body/main/section[1]/div[2]/img/@src")[0],
            plakat_url=plakat_url,
            videos_urls=sorted([url for url in list(urls) if ".mp4" in url]),
        )

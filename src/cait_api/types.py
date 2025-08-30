"""Классы для типизации."""

from dataclasses import dataclass


@dataclass
class CAIT:
    """Объект разговора о важном."""

    title: str
    image_url: str
    date: str
    plakat_url: str
    videos_urls: list[str]

# cait-api

```
- c onversations - разговоры
- a bout         - о
- i mportant     - важных
- t hings        - вещах
```

Неофициальнst **api** "разговоров о важном".

## Использование библиотеки

1. Устанавливаем библиотеку:

``` bash
# Используя pip
pip install git+https://github.com/iamlostshe/cait-api

# Используя uv
uv add git+https://github.com/iamlostshe/cait-api

# Используя poetry
poetry add git+https://github.com/iamlostshe/cait-api
```

2. Запустите код ниже:

``` python
import asyncio
import datetime as dt

from cait_api import CAITParser


def get_next_date() -> str:
    """Получаем ссылку для парсинга."""
    # Получаем текущую дату
    now = dt.datetime.now()

    # Меняем дату на следующий понедельник
    now += dt.timedelta(days=7 - now.weekday())

    # Переводим дату в строку и возвращаем её
    return now.strftime("%d-%m-%Y")


async def main() -> None:
    """Запуск парсера."""
    parser = CAITParser()
    await parser.init()

    cait = await parser.get_info(get_next_date())

    print(
        cait.title,
        cait.date,
        cait.image_url,
        cait.plakat_url,
        cait.videos_urls,
        sep="\n",
    )


if __name__ == "__main__":
    asyncio.run(main())
```

Возвращает объект, типа, cait:

### `cait.title` : str

Загловок разговора о важно, пример: "Массовый спорт в России".

### `cait.date`: str

Дата в формате строки, пример: "10 марта 2025".

### `cait.image_url`: str

Ссылка на изображение, пример: "https://разговорыоважном.рф/img/2025/10-03-2025.jpg".

### `cait.plakat_url`: str

Ссылка на плакат, пример: "https://разговорыоважном.рф/10-03-2025/plakat.jpg".

### `cait.videos_urls`: list[str]

Список ссылок на видео, пример: ["https://разговорыоважном.рф/10-03-2025/1.mp4", "https://разговорыоважном.рф/10-03-2025/2.mp4"].

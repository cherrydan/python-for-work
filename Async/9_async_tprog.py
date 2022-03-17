#!/usr/bin/python3
# -*- coding: utf-8 -*-

# асинхронность на event_loop, переделал
# с новыми заморочками с менеджером контестов
# сделаем замер времени
# (примерно от 0.81 до 1.04 с.)

import asyncio
import aiohttp
from time import time

# берём 4 самых известных сайта
urls = ['http://google.com', 'http://mail.ru', 'http://python.org', 'http://yandex.ru']


# получаем http-содержимое сайтов
async def call_url(url):
    """
    call_url(url)
    url - str
    return http-text
    """
    # как раз организация контекста на классах
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print('Starting {}...'.format(url))
            data = await response.text()
            print('{}: {} bytes '.format(url, len(data)))
        return data


if __name__ == '__main__':
    futures = [call_url(url) for url in urls]
    t0 = time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))
    print('\nTime elapsed: ' + str(time() - t0) + ' sec.')

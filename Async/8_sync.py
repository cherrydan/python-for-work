#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Программа скачивает 10 случайных изображений с сайта
https://loremflickr.com/, в синхронном стиле

от 5 до 10 секунд
"""
import requests

from time import time


def get_file(url):
    response = requests.get(url, allow_redirects=True)
    return response


def write_file(response):
    filename = response.url.split('/')[-1]
    with open(filename, 'wb') as FILE:
        FILE.write(response.content)


def main():
    t0 = time()
    url = 'https://loremflickr.com/320/240'

    for i in range(10):
        write_file(get_file(url))

    print(time() - t0)


if __name__ == '__main__':
    main()

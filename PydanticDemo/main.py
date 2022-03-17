#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pydantic import BaseModel, ValidationError, Field, validator
from typing import List


# делаем вложенный класс данных
class Tag(BaseModel):
    id: int
    tag: str


# создаём класс данных, отнаследованый от базовой модели
class City(BaseModel):
    city_id: int
    name: str

    # валидация по полю name - оно может иметь лишь одно значение "SPB"
    @validator('name')
    def only_spb(cls, v: str) -> str:
        if 'spb' not in v.lower():
            raise ValueError('Work only with SPB!')
        return v

    population: int
    tags: List[Tag]
    # создаём псевдоним для совместимости с JavaScript на фронте
    country: str = Field(alias='CountryName')


input_json = """ 
{
"city_id": "1",
"name": "SPB",
"population": "10000000",
"tags": [{"id": 1, "tag": "capital"},
         {"id": 2, "tag": "big_city"}],
 "CountryName": "Russia"
}
"""

# провалидируем данные при помощи исключения ValidateError
# парсим строку, полученную как json
try:
    city = City.parse_raw(input_json)

except ValidationError as err:
    print('Exception: ', err.json())
else:
    # распарсим первый тег
    print(city.tags[0])
    # сделаем обратное - выведем второй тег в виде json
    tag = city.tags[1]
    print(tag.json())
    # несмотря на то, что в порции данных мы получим имя поля в стиле JS
    print(city.json())  # если вывести так, то мы получим имя поля в стиле Python
    # а таким образом в нашем JSON выводе мы получим имя поля в стиле JS
    print(city.json(by_alias=True))
    # исключаем из вывода поле population, теги по умолчанию by_alias = False
    print(city.json(exclude={"population", "tags"}))

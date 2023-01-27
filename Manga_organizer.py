import requests
import pytest
import random
from random import randint
import json

STATIC_DB = "https://my-json-server.typicode.com/toshirohug/Manga_shelf/shonen"
SHONEN_ENDPOINT = "http://localhost:3000/shonen"
SHOJO_ENDPOINT = "http://localhost:3000/shojo"
KODOMOMUKE_ENDPOINT = "http://localhost:3000/kodomoMuke"

@pytest.fixture
def test_random_endpoint():
    endpoints_list = SHONEN_ENDPOINT, SHOJO_ENDPOINT, KODOMOMUKE_ENDPOINT
    random_endpoint = random.choice(endpoints_list)
    return random_endpoint

@pytest.fixture
def random_manga(random_endpoint):
    selected_resource = requests.get(random_endpoint)
    json_data = json.loads(selected_resource.text)
    random_manga = random.choice(json_data)
    return random_manga

manga_to_post = [{'id':55, 'name':'Yuyu Hakusho', 'volume':1}, {'id':17, 'name':'Saint Seiya', 'volume':2}, \
{'id':18, 'name':'Saint Seiya', 'volume':3}, {'id':19, 'name':'Saint Seiya', 'volume':4}, {'id':20, 'name':'Saint Seiya', 'volume':5}]

@pytest.mark.parametrize('manga', manga_to_post)
def test_01_storing_manga(random_endpoint, manga):

    store_manga_response = requests.post(random_endpoint, manga)
    print(store_manga_response)
    assert store_manga_response.status_code == 201, "Check if the manga alread exists."

def test_atualiza_resource(random_endpoint, random_manga):

    manga_id = randint(0, 5)
    random_endpoint = "{}/{}".format(random_endpoint, manga_id)
    print(random_endpoint)
    print(random_manga)
    put_manga_response = requests.put(random_endpoint, data = random_manga)
    print(put_manga_response.text)

shonen_manga_data = [(1, 'Blue Lock', 1), (2, 'Blue Lock', 2), (3, 'Blue Lock', 3), (4, 'Blue Lock', 4), (5, 'Blue Lock', 5)]

@pytest.mark.parametrize('manga_id, expected_manga_name, expected_manga_volume', shonen_manga_data)
def test_04_check_all_shonen_mangas(manga_id, expected_manga_name, expected_manga_volume):
    response = requests.get(f'https://my-json-server.typicode.com/toshirohug/Manga_shelf/shonen/{manga_id}')
    body = response.text

    str_expected_manga_volume = str(expected_manga_volume)
    
    assert expected_manga_name in body
    assert str_expected_manga_volume in body

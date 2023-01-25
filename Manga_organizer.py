import requests
import pytest

url = "https://my-json-server.typicode.com/toshirohug/Manga_shelf"
payload = {
            "id": 1,
            "name": "Blue Lock",
            "volume": "02",
        }


def test_01_storing_manga():
    store_manga_response = requests.post(url, json=payload)
    assert store_manga_response.status_code == 201
    print(store_manga_response.json())

def test_02_replacing_manga():
    replace_manga_response = requests.put(url, json=payload)
    assert replace_manga_response.status_code == 201
    print(replace_manga_response.json())

def test_03_check_for_singular_manga():
    """
    O que quero é: checar a LISTA_DE_DICIONARIOS por um VALOR e caso exista, IMPRIMIR o respectivo DICIONÁRIO
    """
    payload_wanted_manga =payload.get('name', 'Blue Lock')
    print(payload_wanted_manga)
    # check_manga_response = requests.get(url, json=payload_wanted_manga) 
    # print(check_manga_response.json())
    # assert check_manga_response.status_code == 200

@pytest.mark.parametrize('endpoint, id, name, volume'['/shonen'])
def test_04_check_all_shonen_mangas():
    response = requests.get(url)
    assert response.status_code == 200
    print(response.text)

# def test_02_replacing_manga():
#     replace = requests.put(url, data={"Id": "1", "title": "Blue Lock", "volume": "02", "userId": "10"})
#     print(replace.json())
#     assert replace.status_code == 200

def get_all_mangas():
    response = requests.get(https://my-json-server.typicode.com/toshirohug/Manga_shelf/Shonen)
    shonen_list = response.text

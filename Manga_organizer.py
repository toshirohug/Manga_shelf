import requests
import pytest

url = "https://jsonplaceholder.typicode.com/posts"
payload = {
            "id": "1",
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

def test_03_check_manga():
    check_manga_response = requests.get(url, json=payload()["volume": "02"])
    assert check_manga_response.status_code == 201
    print(check_manga_response.json())
# def test_02_replacing_manga():
#     replace = requests.put(url, data={"Id": "1", "title": "Blue Lock", "volume": "02", "userId": "10"})
#     print(replace.json())
#     assert replace.status_code == 200

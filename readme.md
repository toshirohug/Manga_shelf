# Overview

A manga shelf testing project. Does validate POST | PUT | DELETE calls between either faker API (my-json-server) and JSON server (having instanced another resource to persist request operations).

# Prerequisites

API endpoint need to be Up.

Introduction of python/pytest basics.

Introduction of pytest fixtures.

Knowledge of status code family.

Creating of your API documentation into myjsonserver (see the link listed below in References) -> For this project was generated the entire API [documentation](https://my-json-server.typicode.com/toshirohug/Manga_shelf/).

# SetUp

Visual studio code - [download](https://code.visualstudio.com/download)

Python 3.5 and higher - [download](https://www.python.org/downloads/)

Pytest [Install](https://docs.pytest.org)

Requests [Install](https://requests.readthedocs.io)

## JSON server

Under the folder you launched on Visual studio, enter the following commands (in that order) into terminal (I recommend strongly bash terminal):

```sh
$ mkdir json-server-lib

$ cd json-server-lib

$ npm init -y

$ npm i -g json-server
```

## Starting JSON server

The JSON server is started with the json-server:

```sh
$ json-server --watch mangas.json
```
# Usage

Manga shelf is a API testing project composed of a collection of mangas ordened by categories: for young -> most common themes (Shonen) | for girls (Shojo) | for kids (KodomoMuke). Whenever the shelf owner is visiting their pretty and charming manga corner, he could take a look for appreciation, or grab one and left it at headboard and after, put another manga in the same position which the previous one was. He can also includding new volumes for any collections. Or else, he maybe withraw one of those mangas and for some reason, cannot put back (giving for someone, by loss...). For this purpose, we have the tests wrote to validate the get, put, post and delete calls for the fake API.

# References

[jsonplaceholder API](https://jsonplaceholder.typicode.com/guide/)

[Short guide to use the jsonplaceholder API with myjsonserver (PT)](https://medium.com/code-prestige/como-criar-um-a-api-rest-fake-para-testes-jsonplaceholder-7cc106ea3bd6)

[Json server - a solution to emulating a simple API locally](https://zetcode.com/javascript/jsonserver/)

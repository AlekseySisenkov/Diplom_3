import random

import requests

from data import URL_API, INGREDIENTS


def payload_ing():
    ingredient_id = []
    r_ing = requests.get(URL_API + INGREDIENTS)
    for i in range(len(r_ing.json()['data'])):
        ingredient_id.append(r_ing.json()['data'][i]['_id'])
    return {"ingredients": [random.choice(ingredient_id), random.choice(ingredient_id)]}


def creat_user(ref, data):
    return requests.post(ref, data=data)


def login_user(ref, data):
    return requests.post(ref, data=data, timeout=10)


def delete_user(ref, token):
    requests.delete(ref, headers={'Authorization': token})

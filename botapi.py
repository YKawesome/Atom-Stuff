import requests

query = input("Search: ")
query.replace(" ", "+")

headers = {
    'key': "AIzaSyCt-wqfhbdhhkyBION8YP-lr3ZU6-9_HNQ",
    'apilink': "https://www.googleapis.com/customsearch/v1",
    'cx': "1ffb260c3faceaacd",
    'cr': "countryUS",
    'lr': "lang_en"
    }

response = requests.get(headers['apilink'] + "?key=" + headers['key'] + "&c2coff=1" + "&cr=" + headers['cr'] + "&cx=" + headers['cx'] + "&lr" + headers['lr'] + "&num=3" + "&q=" + query)

data = response.json()

final = data["items"][0]["link"]

print(final)

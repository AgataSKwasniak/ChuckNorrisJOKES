import requests

dane = requests.get("https://api.chucknorris.io/jokes/categories")
x = dane.json()
print(x)

pytanie = input("Z jakiej kategorii chciałbys usłyszeć żart? ")

zart = requests.get(f"https://api.chucknorris.io/jokes/random?category={pytanie}")
y = zart.json()
print(y["value"])



import requests

response = requests.get("https://api.chucknorris.io/jokes/random")

try:
    if response.status_code == 200:
        joke = response.json()['value']
        print("Tässä on sinulle Chunk Norris vitsi, ole hyvä")
        print(joke)

except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")

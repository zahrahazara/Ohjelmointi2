import requests

# Kysy käyttäjältä paikkakunnan nimi
city = input("Anna paikkakunnan nimi: ")

# Anna OpenWeatherMap API-avain
api_key = "f02c6400c64dbe718a901b245017c623"

# Luo API-pyyntö säätilan hakemiseksi
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)
print("Nettiin lähtevä hakulause:")
print(url)
# Tarkista, että vastaus onnistui
try:
    if response.status_code == 200:
    # Tallenna vastauksen json-muotoinen data muuttujaan
     data = response.json()

    # Muunna Kelvin-asteet Celsius-asteiksi
    temperature = data['main']['temp'] - 273.15

    # Tulosta säätilan kuvaus ja lämpötila
    weather = data['weather'][0]['description']
    print(f"Sää paikkakunnalla {city}: {weather}, lämpötila {temperature:.1f} C")

except requests.exceptions.RequestException as e:
    # Jos vastaus epäonnistui, ilmoita käyttäjälle virheestä
    print("Säätiedon hakeminen epäonnistui.")

import requests

url = 'https://api.chucknorris.io/jokes/random'

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if len(data) == 0:
            print("Ei hakutuloksia")
        print(f"{data['value']}")
    else:
        print(f"Viallinen osoite, error: {response.status_code}")
except requests.exceptions.RequestException as e:
    print("Jotain meni pieleen: " + str(e))
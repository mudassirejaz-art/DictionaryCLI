import requests

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def fetch_word(word):
    try:
        response = requests.get(f"{API_URL}{word}")
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError:
        return None
    except Exception as e:
        print(f"[Error] {e}")
        return None
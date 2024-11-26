import requests

def connect_to_synology():
    url = "https://quickconnect.to/krystofserver"
    response = requests.get(url)
    if response.status_code == 200:
        print("Připojeno k Synology NAS")
    else:
        print("Chyba při připojení")
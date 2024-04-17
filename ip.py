import requests

def fetch_public_ip():
        try:
            response = requests.get('https://api.ipify.org')
            public_ip = response.text
            print(f"The public IP address of the server is: {public_ip}")
        except requests.RequestException as e:
            print(f"Error fetching public IP address: {e}")

fetch_public_ip()
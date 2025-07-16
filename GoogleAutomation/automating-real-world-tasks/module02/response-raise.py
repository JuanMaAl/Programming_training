import requests

response = requests.get('https://www.google.es')
response.raise_for_status()
print(response.text)

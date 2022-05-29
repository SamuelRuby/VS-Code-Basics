import requests


ngrok_url = 'https://0a54-2a0c-5a84-3703-6d00-59c2-8b5f-ef77-64c9.eu.ngrok.io'
endpoint = f'{ngrok_url}/box-office-mojo-scraper'

r = requests.post(endpoint, json = {})
print(r.text)
print (r.json()['data'])
import requests

response = requests.get('https://www.google.co.il/')

print(f'{response.elapsed.total_seconds()} seconds')

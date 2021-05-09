import requests

url = 'https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My'
response = requests.get(url)
# new_response = response.url.split('=')
# print(new_response)
# giphys_over_100 = []
# print(response.json()['data'][0]['images']['original'])

for giphy in (response.json()['data']):
    if int(giphy['images']['original']['height']) >= 100:
        giphys_over_100.append(giphy['url'])

print(giphys_over_100)
print(len(giphys_over_100))
print(giphys_over_100[:10])

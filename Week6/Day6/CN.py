import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.find_all('a'))
# print(soup.select(".score"))
# print(soup.select(".storylink"))
links = soup.select('.storylink')
votes = soup.select(".score")

print(soup.select('.subtext')[9])
if '<span class="score" id="score' in str(soup.select('.subtext')[0]):
    print('AAAA')
else:
    print('BBB')


# print(votes[0].get('id'))
# print(votes[0].get('value'))

def create_custom_hn(links, votes):
    hn = []
    soup = BeautifulSoup(response.text, 'html.parser')
    for index, item in enumerate(links):
        if 'class="score"' in str(soup.select('.subtext')[index]):
            points = int(votes[index].getText().replace(' points', ''))
            if points >= 100:
                title = links[index].getText()
                href = links[index].get('href', None)
                hn.append({'title': title, 'link': href, 'score': points})
        # else:
        #     print('BBB')

    # return points


# print(create_custom_hn(links, votes))
create_custom_hn(links, votes)

import requests


# request_url = 'https://api.chucknorris.io/jokes/random'
#
# response = requests.get(request_url)
# # if you are getting no errors (status is 200 for good request)
# if response.status_code == 200:
#     # this is a dictionary wrapping data from the url
#     print(response.json())
#     print(response.json()['value'])
# else:
#     print('BAD REQUEST!')
#
# # if response.status_code == 200:
# # wrong url
# request_url2 = 'https://api.chucknorris.io/jokes/rand'
# response2 = requests.get(request_url2)
#
# if response2.status_code == 200:
#     print(response2.json())
#     print(response2.json()['value'])
# else:
#     print('BAD REQUEST!')

# setting the url from the api webpage
def get_categories(request_url='https://api.chucknorris.io/jokes/categories'):
    # getting the content of the url
    response = requests.get(request_url)

    # asking if the content getting went right(code 200)
    if response.status_code == 200:
        return response.json()
    else:
        print('BAD REQUEST!')
        return


def get_joke_by_category():
    # getting the categories from the original function
    categories = get_categories()
    categories = ('\n').join(categories) + '\n'
    user_choice = input(f'Pick a category from {categories} ')

    while user_choice not in categories:
        user_choice = input(f'Pick a category from {categories} ')

    # giving to the url the users choice
    url = f'https://api.chucknorris.io/jokes/random?category={user_choice}'
    # setting "response" to get the data (dict) from the website api
    response = requests.get(url)
    # if everything went right, print the category based joke
    if response.status_code == 200:
        print(response.json()['value'])


get_joke_by_category()



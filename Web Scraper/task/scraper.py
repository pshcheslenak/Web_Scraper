import requests

# url = 'http://api.quotable.io/quotes/-CzNrWMGIg8V'

url = input()
response = requests.get(url)

if response:
    # print(response)
    try:
        print(response.json()['content'])
    except KeyError:
        print('Invalid quote resource!')
else:
    print('Invalid quote resource!')

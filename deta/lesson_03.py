import requests
from bs4 import BeautifulSoup

url = 'https://scraping-for-beginner.herokuapp.com/udemy'
res = requests.get(url)
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.find_all('p'))
# subscribers = soup.find_all('class', attrs={'subscribers'})[0]
# print(subscribers)
# n_sub = int(subscribers.text.split(':')[1])


# reviews = soup.find_all('p', attrs={'class', 'reviews'})[0]
# n_reviews = int(reviews.text.split(':')[1])
# print(n_reviews)

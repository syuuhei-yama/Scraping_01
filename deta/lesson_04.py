import requests
from bs4 import BeautifulSoup

url = 'https://scraping-for-beginner.herokuapp.com/ranking/'
res = requests.get(url)
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)

#観光地名
spots = soup.find_all('div', attrs={'class','u_areaListRankingBox'})
spot = spots[0]
# spot_name = spot.find_all('div', attrs={'class','u_title'})
# print(spot_name.find('span',attrs={'class', 'badge'}))

#評点
cotegoryItems = spot.find_all('div', attrs={'class','u_categoryTipsItem'})
cotegoryItems = cotegoryItems.dl.text
print(cotegoryItems)

import requests
from bs4 import BeautifulSoup

url = 'https://p-nt-www-amazon-in-kalias.amazon.in/New-Apple-iPhone-12-128GB/dp/B08L5VJWCV?th=1'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

reviews = []
for review in soup.find_all('div', {'class': 'review'}):
    rating = review.find('span', {'class': 'a-icon-alt'}).text
    text = review.find('span', {'class': 'review-text'}).text
    reviews.append({'rating': rating, 'review': text})

print(type(reviews))

for key, value in reviews:
    print("Key: ", key)
    print("Value : ", value.encode('utf-8'))

print(response.content)
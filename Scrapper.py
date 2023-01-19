import requests
from bs4 import BeautifulSoup

url = 'https://p-nt-www-amazon-in-kalias.amazon.in/New-Apple-iPhone-12-128GB/dp/B08L5VJWCV?th=1'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

reviews = []
for review in soup.find_all('div', {'class': 'review'}):
    name = review.find('span', class_ = "a-profile-name").text
    star = review.find('span', class_ = "a-icon-alt").text
    date = review.find('span', class_ = "a-size-base a-color-secondary review-date").text
    comment = review.find('a', class_ = "a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold").text.strip()
    body = review.find('div', class_ = "a-expander-content reviewText review-text-content a-expander-partial-collapse-content").text.strip()
    img_links = []
    vote = review.find('span', class_ = "a-size-base a-color-tertiary cr-vote-text")
    variant = review.find('span', {'data-hook': 'format-strip-linkless'})

    product_name = "Not Available"
    size = "Not Available"
    colour = "Not Available"
    # Filtering the 'None' type data..
    if vote != None:
      vote = vote.text
    if variant != None:
      variant = variant.text
      temp, product_name = str(variant).split("Pattern name: ")
      temp, size = temp.split("Size: ")
      temp, colour = temp.split("Colour: ")
    if review.find('div', class_ = "review-image-tile-section") == None:
      img_links.append("Not Available")
    else:
      raw_img_links = review.find_all('img', alt = "Customer image")
      for individual_links in raw_img_links:
        media_link = individual_links.get('data-src')
        if media_link != None:
          img_links.append(media_link)

    # Printing the details..
    print("\n\n\n\nNAME      :   ", name)
    print("PRODUCT   :   ", product_name)
    print("COLOUR    :   ", colour)
    print("SIZE      :   ", size)
    print("STAR      :   ", star)
    print("DATE      :   ", date.encode("utf-8"))
    print("COMMENT   :   ", comment.encode("utf-8"))
    print("BODY      :   ", body.encode("utf-8"))
    print("IMAGES    :   ", img_links)
    print("VOTE      :   ", vote)

#print(type(reviews))
#print(len(reviews))

#for key, value in reviews:
#    print("Key: ", key)
#    print("Value : ", value.encode('utf-8'))

#print(response.content)
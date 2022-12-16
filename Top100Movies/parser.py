import requests
from bs4 import BeautifulSoup
from time import sleep

url = "https://www.kinoafisha.info/rating/movies/"
r = requests.get(url)

data = []
top = 0

soup = BeautifulSoup(r.text, 'html.parser')

films = soup.findAll('div', class_='movieList_item movieItem movieItem-rating movieItem-position')
for film in films:
    top+=1
    title = film.find('a', class_='movieItem_title').text
    desc = film.find('span', class_='movieItem_year').text
    img = film.find('picture', class_='movieItem_poster picture picture-poster').find('img', class_='picture_image').get('data-picture')
    data.append([title,desc,top,img])


import requests
from bs4 import BeautifulSoup
import csv
from random import randint
from time import sleep
import sqlite3

conn = sqlite3.connect( "caars.sqlite" )
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS cars
          (id INTEGER PRIMARY KEY AUTOINCREMENT,
          img VARCHAR,
          title VARCHAR(50),
          text VARCHAR(200),
          price FLOAT,
          url VARCHAR)
          ''')

i = 1
while i==1:
    url = "https://www.auto.ge/auto.html/" + str(i)
    resp = requests.get(url)
    text = resp.text
    soup = BeautifulSoup(text, 'html.parser')
    body = soup.find('body')
    cars_section = body.find('section',id='listings',class_='list row')
    cars_list = cars_section.find_all('article')
    # print(cars_list)
    for car in cars_list:
        info = car.find('ul', {'class', 'ad-info'})
        car_title = info.find('li', {'class', 'title'})
        title = car_title.a.text.replace('\n', '')
        div = car.find ( 'div',class_='main-column clearfix' )
        a = div.find('a')
        div2 = a.find('div')
        img = div2.img['src']
        print(img)
        car_url = car_title.a['href']
        short_disc = car.find('li', {'class', 'fields'}).text
        price = car.find('li', {'class', 'system'}).text.replace(',','')
        price = price.replace('\n','')
        cursor.execute ( "insert into cars(img, title, text, price, url) "
                         "values(?,?,?,?,?)", (img,title, short_disc, price, car_url))
        conn.commit()
        i += 1
        sleep(randint(15, 20))


import requests
from bs4 import BeautifulSoup
import csv
from random import randint
from time import sleep

url = "https://www.auto.ge/auto.html"
file = open('autos.csv', 'w', encoding='utf-8_sig', newline='\n')
obj = csv.writer(file)
obj.writerow(['დასახელება', 'ფასი', 'მოკლე აღწერა', 'ლინკი'])

for i in range(1, 5):
    url1 = url + str(i)
    resp = requests.get(url1)
    text = resp.text
    soup = BeautifulSoup(text, 'html.parser')
    cars_section = soup.find('section', {'class': 'list row', 'id': 'listings'})
    if cars_section is not None:
        cars_list = cars_section.find_all('article')
        for car in cars_list:
            info = car.find('ul', {'class', 'ad-info'})
            car_title = info.find('li', {'class', 'title'})
            title = car_title.a.text
            car_url = car_title.a['href']
            short_disc = car.find('li', {'class', 'fields'}).text
            price = car.find('li', {'class', 'system'}).text.replace(',''')
            obj.writerow([title,short_disc, price])
    sleep(randint(15, 20))



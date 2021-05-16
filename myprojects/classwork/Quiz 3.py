import requests
import json

url = "https://fitness-calculator.p.rapidapi.com/idealweight"

querystring = {"gender":"female","height":"162","weight":"46"}

headers = {
    'x-rapidapi-key': "5761c8ff7amsh1715f5bccd9d0b5p1b9a9ejsn29c903c74dc6",
    'x-rapidapi-host': "fitness-calculator.p.rapidapi.com"
    }


resp = requests.request("GET", url, headers=headers, params=querystring)

# print(resp)
# print(resp.text)
# print(resp.status_code)
# print(resp.content)
# print(type(resp.content))
# print(resp.headers)


res = json.loads(resp.text)
# my_file = open("Fitness.json", "w+")
# json.dump(res,my_file, indent=4)
# my_file.close()


# პრინტავს იდეალურ წონას პარამეტრების შესაბამისად ერთ-ერთი მეთოდის, კერძონ Devine-ს მეთოდის მიხედვით.
# print(round(res['Devine']))

# ბაზაში ინფორმაციის შეტანა
# newActorsFromUser = [(
#     input('ოსკარის აღების წელი: \n'),
#     input('მსახიობის ასაკი: \n'),
#     input('მსახიობის სახელი და გვარი: \n'),
#     input('მსახიობის სქესი: \n'),
#     input('ფილმის სახელი: \n'),
#
# )]

# ეს ნაწილი ქმნის ბაზას და ცხრილს,რომელშიც მომხმარებლის შეყვანილი მონაცემების მიხედვით ბაზაში ემატება მონაცემები მისი მონაცემები და მისთვის იდეალური წონა.
import sqlite3
conn = sqlite3.connect("fitness.sqlite")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS ideal_weight
          (id INTEGER PRIMARY KEY AUTOINCREMENT,
          gender VARCHAR(50),
          height INTEGER ,
          weight INTEGER ,
          ideal_weight INTEGER )
          ''')
idealWeight = round(res['Devine'])
paramsFromUser =[(
    input('Enter your gender: \n'),
    input('Enter your height: \n'),
    input('Enter your weight: \n'),
    idealWeight
)]

c.executemany('INSERT INTO ideal_weight (gender,height,weight,ideal_weight) VALUES (?,?,?,?)',paramsFromUser)

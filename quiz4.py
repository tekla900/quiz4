from bs4 import BeautifulSoup
import requests
from time import sleep
from random import randint
import csv

payload = {'page': 1}

url = 'https://www.goodreads.com/list/show/114319.Best_Science_Fiction_of_the_20th_Century'


file = open('goodreads.csv', 'w', newline='\n', encoding="utf-8")

file_obj = csv.writer(file)
file_obj.writerow(['Title', 'Author', 'Ranking'])

while payload['page'] <= 5:

    r = requests.get(url, params=payload)
    content = r.text

    soup = BeautifulSoup(content, 'html.parser')

    block = soup.find('table', class_='tableList js-dataTooltip')
    all_books = soup.find_all('td', {'width': '100%', 'valign':'top'})

    for each in all_books:
        title = each.span.text
        author = each.find('a', class_='authorName').text
        rating = each.find('span', class_='minirating').text
        rating = (rating[0:5]).replace(' ', '')
        # print(title, author, rating)
        file_obj.writerow([title, author, rating])
    payload['page'] += 1
    sleep(randint(15, 20))

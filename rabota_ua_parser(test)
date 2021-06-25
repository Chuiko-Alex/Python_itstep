import requests
from bs4 import BeautifulSoup
import fake_useragent


user = fake_useragent.UserAgent().random
HEADERS = {'user-agent': user}
URL = f'https://rabota.ua/zapros/it/%d1%85%d0%b0%d1%80%d1%8c%d0%ba%d0%be%d0%b2/pg'
work_info = []

def get_html(URL, HEAD=HEADERS):
    for page in range(1, 10):
        r = requests.get(url=f'{URL}{page}', headers=HEAD).text
        soup = BeautifulSoup(r, 'html.parser')
        items = soup.find_all('div', class_='card-body')
        for item in items:
            name = item.find('a', class_='ga_listing').get_text()
            company = item.find('a', class_='company-profile-name').get_text()
            city = item.find('span', class_='location').get_text()
            info = item.find('div', class_='card-description').get_text()
            link = item.find('a', class_='ga_listing').get('href')
            work_info.append({'Name':name, 'Company':company, 'City':city, 'Info':info, 'Link':f'https://rabota.ua{link}'})
    return work_info


res = get_html(URL, HEADERS)
f = open('work.csv', 'wt', encoding='utf-8')
for work in res:
    print()
    f.write(work['Name'] + ';')
    f.write(work['Company'] + ';')
    f.write(work['City'] + ';')
    f.write(work['Info'] + ';')
    f.write(work['Link'] + ';\n')
f.close()

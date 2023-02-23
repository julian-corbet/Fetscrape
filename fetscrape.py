#module import#
import requests
from bs4 import BeautifulSoup
import csv
import time

#prepare csv#
exportcsv = open('Fetscrape.csv', 'w', newline='')
csvwriter = csv.writer(exportcsv)
csvwriter.writerow(['User ID', 'Username', 'Age', 'Gender', 'Role', 'Location', 'Extras', 'Link'])

headers = {'user-agent': """Mozilla/5.0 (X11; Linux x86_64) """
                         """AppleWebKit/537.36 (KHTML, like Gecko) """
                         """Chrome/58.0.3029.110 Safari/537.36"""}
#login#
login_data = {
    'user[login]': '',
    'user[password]': '',
    'user[locale]': 'en',
    'user[otp_attempt]': 'step_1',
    'utf8': '✓'
}

with requests.Session() as s:
    url = 'https://fetlife.com/users/sign_in'
    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    login_data['authenticity_token'] = soup.find('input', attrs={'name': 'authenticity_token'})['value']
    r = s.post(url, data=login_data, headers=headers)

#target definition#
for i in range(10):
    r2 = s.get('https://fetlife.com/p/germany/berlin/kinksters?page={}'.format(i+1), headers=headers)
    soup = BeautifulSoup(r2.content, 'lxml')

    #scrape data#
    for results in soup.find_all('div', class_ ='w-100 br1 pointer bg-animate hover-bg-gray-950 bg-gray-900'):
        userID = results.find('a', {"class": 'relative overflow-hidden dib link'})
        ID = (userID['href'])
        ID = ID.split('/')[2]
        print(ID)
        nickname = userID.get('title')
        print(nickname)
        details = results.find('span', {"class": 'f6 fw7 gray-300'}).text
        age_gender = details.split(' ')[0]

        # Capture length of digits (or escape when 4 digits long, prevents infinite loop where gender is omitted)
        j = 1
        while (age_gender[0:j].isdigit() and j <= 4): j += 1

        # Offset pointer
        j -= 1
        age = age_gender[0:j]
        gender = age_gender[j:]

        role = details.split(' ')[1]
        print(age)
        print(gender)
        print(role)
        place = results.find('div', {"class": 'f6 lh-copy fw4 gray-300 nowrap truncate'}).text
        place = place.replace(',', '')
        print(place)
        extras = results.find('div', {"class": 'f6 fw4 lh-copy gray-500 nowrap truncate'}).text
        print(extras)
        link = f"https://fetlife.com/users/{ID}"
        print(link)

        print()

        # export to csv#
        csvwriter.writerow([ID, nickname, age, gender, role, place, extras, link])

        time.sleep(1)


exportcsv.close()

import bs4
import requests

url = 'https://jadwalsholat.pkpu.or.id/'
contents = requests.get(url)

response = bs4.BeautifulSoup(contents.text, "html.parser")
data = response.find_all('tr', 'table_highlight')
data = data[0]

sholat = {}
for d in data:
    print(d.get_text())

i = 0
for a in data:
    if i == 1:
        sholat['Shubuh'] = a.get_text()
    elif i == 2:
        sholat['Dzuhur'] = a.get_text()
    elif i == 3:
        sholat['Ashar'] = a.get_text()
    elif i == 4:
        sholat['Maghrib'] = a.get_text()
    elif i == 5:
        sholat['Isya'] = a.get_text()
    i += 1


print(f'\n{sholat}')
print(sholat['Ashar'])

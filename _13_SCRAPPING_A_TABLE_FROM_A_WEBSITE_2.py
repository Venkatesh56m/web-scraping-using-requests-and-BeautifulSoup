import requests
import pandas as pd
from bs4 import BeautifulSoup

url_12 = "https://ticker.finology.in/"
r_12 = requests.get(url_12)
print(r_12)

soup = BeautifulSoup(r_12.text,'lxml')

table = soup.find("table", class_= "table table-sm table-hover screenertable")
#print((table))

header_table = table.find_all("th")

print(header_table)
titles = []
for i in header_table:
    title = i.text.strip()
    titles.append(title)
#print(titles)

df = pd.DataFrame(columns=titles)
print(df)

rows = table.find_all("tr")
#print(rows)

for i in rows[1:]:
    print(i)
    print(i.text)


for i in rows[1:]:
    data = i.find_all("td")
    #print(data)
    row = [tr.text.strip() for tr in data]
    print(row)
    l = len(df)
    df.loc[l] = row

print(df)

df.to_csv(r"D:\BS4_PDF\bs4_scrapping_first.csv")
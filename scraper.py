from bs4 import BeautifulSoup
import requests
import csv
import sys


START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
request = requests.get(START_URL)

soup = BeautifulSoup(request.text, "html.parser")

headers = ["name","distance","mass","radius"]
star_data = []


temp_list = []

for tr in soup.find("table").find_all("tr"):
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    
    temp_list.append(row)


for i in range(1, len(temp_list)):

    # Checking that the radius is know or not
    
    data = [temp_list[i][1], temp_list[i][3], temp_list[i][5], temp_list[i][6]]
    star_data.append(data)

with open("final.csv", "w", encoding='utf8') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)
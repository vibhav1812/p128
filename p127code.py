import bs4
from bs4 import BeautifulSoup
import time, csv
import requests

url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
headers = ["name", "distance", "mass", "radius"]
star_data = []
# Make a GET request to the webpage
response = requests.get(url)

# Parse the html content of the webpage
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the table rows in the table
table_rows = soup.find('table').find_all('tr')

# Iterate through the rows and print the cells
data_set = []
for row in table_rows:
    cells = row.find_all('td')
    cell_texts = []
    for cell in cells:
        cell_texts.append(cell.text)
    data_set.append(cell_texts)
data_set = data_set[1:]

final_data = []
for specific_cells in data_set:
    indices = [1,3,5,6] 
    data = [specific_cells[i] for i in indices]
    final_data.append(data)

clean_final_data = []
for data in final_data:
    data = [element.strip() for element in data]
    clean_final_data.append(data)

with open("p127(stars).csv", "a+") as f:
    csv_data = csv.writer(f)
    csv_data.writerow(headers)
    csv_data.writerows(clean_final_data)
from selenium import webdriver
from bs4 import BeautifulSoup
import time, csv
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

star_table = soup.find_all('table')
table_rows = star_table[7].find_all('tr')


field_brown_dwarf_data_set = []
for row in table_rows:
    cells = row.find_all('td')
    cell_texts = []
    for cell in cells:
        cell_texts.append(cell.text)
    field_brown_dwarf_data_set.append(cell_texts)
field_brown_dwarf_data_set = field_brown_dwarf_data_set[1:]

final_field_brown_dwarf_data_set = []
for specific_cells in field_brown_dwarf_data_set:
    indices = [0,5,7,8] 
    data = [specific_cells[i] for i in indices]
    final_field_brown_dwarf_data_set.append(data)

clean_final_field_brown_dwarf_data_set = []
for data in final_field_brown_dwarf_data_set:
    data = [element.strip() for element in data]
    clean_final_field_brown_dwarf_data_set.append(data)

df = pd.DataFrame(clean_final_field_brown_dwarf_data_set, columns=["name", "distance", "mass", "radius"])
print(df)
df.to_csv("field_brown_dwarf_data", index=False)
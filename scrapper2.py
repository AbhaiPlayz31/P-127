from bs4 import BeautifulSoup as bs
import time
import csv
import requests
import pandas as pd 

startUrl = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page= requests.get(startUrl)
print(page)


soup = bs(page.text,'html.parser')
star_table= soup.find("table")

temp_list = []

table_row = star_table.find_all("tr")

for tr in table_row:
    td = tr.find_all("td")
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)

star_names = []
distance = []
mass = []
radius = []

    
for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    
    

df2= pd.DataFrame(list(zip(star_names,distance,mass,radius)),columns=["star_names","distance","mass","radius"])

print(df2)

df2.to_csv("scrapper_4.csv")
















# def scrap():
#     headers = ["Proper Name", "Distance (ly)", "Mass", "Radius"]

#     planet_data = []

#     for i in range(0,492):

#         soup = BeautifulSoup(browser.page_source, "html.parser")

#         for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
#             li_tags = ul_tag.find_all("li")
#             temp_list = []

#             for index, li_tags in enumerate(li_tags):
#                 if index == 0:
#                     temp_list.append(li_tags.find_all("a")[0].contents[0])
#                 else:
#                     try:
#                         temp_list.append(li_tags.content[0])
#                     except:
#                         temp_list.append("")
#             planet_data.append(temp_list)
#         browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

#     with open("scrapper_3.csv", "w") as f: 
#         csvwriter = csv.writer(f) 
#         csvwriter.writerow(headers) 
#         csvwriter.writerows(planet_data)
        
# scrap()
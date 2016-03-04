# An example for getting newly loaded content
# http://stackoverflow.com/q/35804751/1585957
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.get("http://localhost:8000/35736910/html/")

# use selenium to get the html
html = driver.page_source

# pass it to beautifulsoup
soup = BeautifulSoup(html)
# first we could find the div that the table is located in
table_div = soup.find("div", {"class" : "content"})
# find the table in this div
table = table_div.find("table")
# get the table body
tbody = table.find("tbody")
# grab all the rows
rows = tbody.findAll("tr")
# loop through the rows
for row in rows:
	td = row.findAll("td")
	# get the column with the data
	td = td[1]
	# extract the elements you don't want
	b = td.find("b")
	b.extract()
	sc = td.find("script")
	sc.extract()
	# print just the number
	print(td.text.strip())

driver.close()
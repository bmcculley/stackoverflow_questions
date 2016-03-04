# An example for getting newly loaded content
# http://stackoverflow.com/q/35804751/1585957
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
driver.get("http://localhost:8000/")
assert "Selenium Test" in driver.title
print driver.page_source
sleep(18)
print driver.page_source

driver.close()
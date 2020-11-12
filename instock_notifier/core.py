import json
import chromedriver_binary
import os

import config
import helpers
import utils

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def main():
    while (True):
        check_stock_changes()

        if not config.RECURRING:
            break

        sleep(config.RECURRENCE_INTERVAL_INMINUTES * 60)

def check_stock_changes():

	products = get_product_list()

	if len(products) > 0:
		driver = webdriver.Chrome()

	for product in products:
		try:
			if bool(product["skip"]) == False:
				send_email = False
				driver.get(product["url"])
				sleep(2)
				
				found = driver.find_elements_by_css_selector(product["lookfor"])
				
				if len(found) > 0 and bool(product["notifyiffound"]) == True:
					send_email = True
				elif len(found) == 0 and bool(product["notifyiffound"]) == False:
					send_email = True
				else:
					print('Out of stock')

				if send_email and helpers.must_notify(product["url"]):
					helpers.notify(product["url"])
		except Exception as e:
			print(e)

	driver.close()
	driver.quit()
    
def get_product_list():
    with open('products.json', 'r') as myfile:
        products = myfile.read()

    return json.loads(products)
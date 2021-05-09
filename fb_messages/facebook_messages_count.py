print('Loading Libraries...')
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

print('Finished loading libraries.')

op = webdriver.ChromeOptions()
#op.add_argument('headless')
print('Loading browser...')
driver = webdriver.Chrome('./chromedriver',options=op)
print("Finished loading browser.")

location = "Miami--FL"
category = "nature-and-outdoors"
url = f'https://fr.airbnb.com/s/{location}/experiences/{category}'

usr='dimitrisoumpasis@gmail.com'
pwd='09102000' 

driver.get('https://www.facebook.com/')
print ("Opened facebook")
sleep(1)
  
username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)
print ("Email Id entered")
sleep(1)
  
password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print ("Password entered")
  
login_box = driver.find_elements_by_tag_name('button')[0]
login_box.click()

try:
	dates = []
	print('waiting elements...')
	elements = WebDriverWait(driver, 10).until(cond.visibility_of_all_elements_located((By.TAG_NAME, 'a')))
	for e in elements:
		print(e.get_attribute("aria-label"))
	divs = driver.find_elements_by_tag_name('div')
	for div in divs:
		if div.get_attribute("aria-label") is not None:
			if div.get_attribute('aria-label').find('Messenger') != -1:
				print(div.get_attribute('aria-label'))
				break
	print('nothing')
except:
	divs = driver.find_elements_by_tag_name('div')
	for div in divs:
		if div.get_attribute("aria-label") is not None:
			if div.get_attribute('aria-label').find('Messenger') != -1:
				print(div.get_attribute('aria-label'))
				break
	print('nothing')
	print('closed')
		

print("Finished")

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

usr='biosoinbeauty'
pwd='cocojumbo06' 

driver.get('https://www.instagram.com/')
print ("Opened instagram")
sleep(1)
  
username_box = driver.find_element_by_xpath("//input[@name='username']")
username_box.send_keys(usr)
print ("Email entered")
sleep(1)
  
password_box = driver.find_element_by_xpath("//input[@name='password']")
password_box.send_keys(pwd)
password_box.send_keys(u'\ue007')
print ("Password entered")


try:
	dates = []
	print('waiting elements...')
	elements = WebDriverWait(driver, 5).until(cond.visibility_of_all_elements_located((By.CLASS_NAME, 'Fifk5')))
	messages = 0
	for e in elements:
		if e.text != "\n" and e.text != '':
			#print("".join(e.text.split()))
			messages = int("".join(e.text.split()))
	print(f'{messages} messages found')
except:
	elements = driver.find_elements_by_tag_name('a')
	for e in elements:
		if e.get_attribute("aria-label") is not None:
			if e.get_attribute("aria-label").find("Notifications,") != -1:
				print(e.get_attribute("aria-label"))
	print('exception')
		

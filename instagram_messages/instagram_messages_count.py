from time import sleep			#Libraries used are 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def instagram_messages_count():
	op = webdriver.ChromeOptions() 	#Here the scipt loads the chrome browser
	op.add_argument('--disable-notifications')
	# op.add_argument('headless')
	driver = webdriver.Chrome(ChromeDriverManager().install(),options=op)

	driver.get('https://www.instagram.com/')#Opens instagram page

	try:
		element = WebDriverWait(driver,600).until(cond.element_to_be_clickable((By.CSS_SELECTOR, 'path[d="M47.8 3.8c-.3-.5-.8-.8-1.3-.8h-45C.9 3.1.3 3.5.1 4S0 5.2.4 5.7l15.9 15.6 5.5 22.6c.1.6.6 1 1.2 1.1h.2c.5 0 1-.3 1.3-.7l23.2-39c.4-.4.4-1 .1-1.5zM5.2 6.1h35.5L18 18.7 5.2 6.1zm18.7 33.6l-4.4-18.4L42.4 8.6 23.9 39.7z"]')))
		try:
			nOfMsg = driver.find_element_by_class_name('bqXJH')
			return("You have " + nOfMsg.get_attribute('innerHTML') + " new message(s)")
		except:
			return("No new messages found")
	except:
		return('timeout')


from time import sleep			#Libraries used are 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def facebook_messages_count():
	op = webdriver.ChromeOptions() 	#Here the scipt loads the chrome browser
	op.add_argument('--disable-notifications')
	# op.add_argument('headless')
	driver = webdriver.Chrome(ChromeDriverManager().install(),options=op)

	driver.get('https://www.facebook.com/')#Opens facebook page

	try:
		element = WebDriverWait(driver,600).until(cond.element_to_be_clickable((By.CSS_SELECTOR, 'path[d="M14 2.042c6.76 0 12 4.952 12 11.64S20.76 25.322 14 25.322a13.091 13.091 0 0 1-3.474-.461.956 .956 0 0 0-.641.047L7.5 25.959a.961.961 0 0 1-1.348-.849l-.065-2.134a.957.957 0 0 0-.322-.684A11.389 11.389 0 0 1 2 13.682C2 6.994 7.24 2.042 14 2.042ZM6.794 17.086a.57.57 0 0 0 .827.758l3.786-2.874a.722.722 0 0 1 .868 0l2.8 2.1a1.8 1.8 0 0 0 2.6-.481l3.525-5.592a.57.57 0 0 0-.827-.758l-3.786 2.874a.722.722 0 0 1-.868 0l-2.8-2.1a1.8 1.8 0 0 0-2.6.481Z"]')))
		divs = driver.find_elements_by_tag_name('div')
		try:
			for div in divs:
				if div.get_attribute("aria-label") is not None:
					if div.get_attribute('aria-label').find('Messenger') != -1:
						if(len(div.get_attribute('aria-label')) == 9):
							return('No message found')
						else:
							res = [int(s) for s in div.get_attribute('aria-label').split() if s.isdigit()]
							return("You have " + str(res[0]) + " unread message(s)")
		except:
			return("*1")
	except:
		return('timeout')

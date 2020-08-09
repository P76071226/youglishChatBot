import requests
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

youeng_url = 'https://youglish.com/'
searchword = 'show off'
searchword=searchword.replace(' ', '%20')
my_url = 'https://youglish.com/pronounce/' + searchword + '/english?'

driver.get(my_url)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="gdprModal"]/div[2]/div/div[3]/button').click()

youtube_url = driver.find_element_by_id('player').get_attribute('src')

driver.close()
driver.quit()

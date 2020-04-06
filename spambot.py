import warnings
warnings.filterwarnings('ignore')
from selenium import webdriver
import time

#text that will appear as spam
text = 'spam text here'

#the question it will show they supposedly asked (only available for iOS users currently. Leave empty if not being used
customQuestions = ''

#number of spam messages
messageNum = 50

#url in this format, up until the '?w='
url = 'https://onyolo.com/m/qWExC3fgnEr'




if len(customQuestions) > 0:
    url = url + '?w=' + customQuestions



driver = webdriver.PhantomJS()
driver.get(url)
for x in range(0,messageNum):

    driver.find_element_by_id('text').send_keys(text)

    driver.find_element_by_id('send-button').click()
    time.sleep(1)
    driver.refresh()

driver.quit()

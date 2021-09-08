from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# browser = webdriver.Chrome(ChromeDriverManager().install())
# browser.get('https://www.google.co.jp/')
# url = 'https://scraping-for-beginner.herokuapp.com/login_page'
# browser.get(url)
# elem_username = browser.find_element_by_id('username')
# elem_password = browser.find_element_by_id('password')
# elem_username.send_keys('imanishi')
# elem_password.send_keys('kohei')
# elem_login_btn = browser.find_element_by_id('login-btn')
# elem_login_btn.click()
# browser.quit()

#流れ
browser = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://scraping-for-beginner.herokuapp.com/login_page'
browser.get(url)
sleep(4)
elem_username = browser.find_element_by_id('username')
elem_username.send_keys('imanishi')

elem_password = browser.find_element_by_id('password')
elem_password.send_keys('kohei')

sleep(1)
elem_login_btn = browser.find_element_by_id('login-btn')
elem_login_btn.click()






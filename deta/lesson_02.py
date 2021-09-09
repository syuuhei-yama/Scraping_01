from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

#ログイン情報入力
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://scraping-for-beginner.herokuapp.com/login_page')
elem_username = browser.find_element_by_id('username')
elem_username.send_keys('imanishi')
elem_password = browser.find_element_by_id('password')
elem_password.send_keys('kohei')

#クリックする
elem_login_btn = browser.find_element_by_id('login-btn')
elem_login_btn.click()

#テキストデータ取得
# elem = browser.find_element_by_id('name')
# print(elem.text)
#
# elem_company = browser.find_element_by_id('company')
# print(elem_company.text)
#
# elem_birthday = browser.find_element_by_id('birthday')
# print(elem_birthday.text)
#
# elem_come_from = browser.find_element_by_id('come_from')
# print(elem_come_from.text)
#
# elem_hoby = browser.find_element_by_id('hobby')
# print(elem_hoby.text)

elems_th = browser.find_elements_by_tag_name('th')
# print(elem_th[0].text)
keys = []
for elem_th in elems_th:
    key = elem_th.text
    keys.append(key)
print(keys)

elems_td = browser.find_elements_by_tag_name('td')
# print(elem_th[0].text)
values = []
for elem_td in elems_td:
    value = elem_td.text
    values.append(value)
print(values)

#CSVファイルを作成
df = pd.DataFrame()
df['項目'] = keys
df['値'] = values
df.to_csv('講師情報.csv', index=False)
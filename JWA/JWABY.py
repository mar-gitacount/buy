from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# WebDriverの初期化（Chromeを使用する例）
driver = webdriver.Chrome()

# ログインページに移動
driver.get("https://main.d1dtad27aqmwn9.amplifyapp.com/signin")

# ユーザー名とパスワードを入力してログイン
username_input = driver.find_element_by_id("ichikawa.contact@gmail.com")
password_input = driver.find_element_by_id("111111")
login_button = driver.find_element_by_id("login_button")

username_input.send_keys("ichikawa.contact@gmail.com")
password_input.send_keys("111111")
login_button.click()

# ログイン後のページで作業を続ける（必要に応じて）
# 例えば、ログイン後のページから情報を取得したり、操作を行ったりする

# WebDriverを閉じる
driver.quit()

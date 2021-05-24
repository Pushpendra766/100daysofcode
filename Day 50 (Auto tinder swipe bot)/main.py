from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

MOBILE_NUMBER = YOUR-TINDER-USERNAME #MOBILE NUMBER/EMAIL BY WHICH YOU HAVE FB ACCOUNT
PASSWORD = YOUR-TINDER-PASSWORD #FB PASSWORD

chrome_driver_path = YOUR_DRIVER_PATH_HERE
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://tinder.com/")

#click login button
time.sleep(2)
login = driver.find_element_by_xpath('//*[@id="c-174738105"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()

#choose facebook as option
time.sleep(3)
facebook = driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook.click()

#switch window to facebook login window
time.sleep(3)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

#enter facebook login details
email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys(MOBILE_NUMBER)
password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

#switch window back to base window
driver.switch_to.window(base_window)

time.sleep(10)
location = driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div/div/div[3]/button[1]')
location.click()

notification = driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div/div/div[3]/button[2]')
notification.click()

time.sleep(7)
for n in range(30):
    time.sleep(1)
    try:
        print("Called")
        dislike = driver.find_element_by_xpath('//*[@id="c-174738105"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button')
        dislike.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)
driver.quit()
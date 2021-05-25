from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

CHROME_DRIVER_PATH = YOUR_CHROME_DRIVER_PATH
USERNAME = input("Enter your username : ")
PASSWORD = input("Enter your password : ")
SIMILAR_ACCOUNT = input("Similar Account's Username : ")

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        sleep(5)
        username = self.driver.find_element_by_name("username")
        username.send_keys(USERNAME)
        password = self.driver.find_element_by_name("password")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(5)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        sleep(5)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        
        sleep(5)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

        for i in range(3):
            self.follow()
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        follows = self.driver.find_elements_by_css_selector("li button")
        for follow in follows:
            try:
                follow.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel.click()



instabot = InstaFollower()
instabot.login()
instabot.find_followers()


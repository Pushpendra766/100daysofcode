from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = YOUR_DRIVER_PATH_HERE
TWITTER_USER = TWITTER_USERNAME
TWITTER_PASSWORD = TWITTER_PASSWORD


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(5)
        go = self.driver.find_element_by_css_selector(".start-button a")
        go.click()
        sleep(50)
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        # self.driver.quit()

    def tweet_at_provider(self, tweet_text):
        self.driver.get("https://twitter.com/login")
        sleep(2)
        username = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        username.send_keys(TWITTER_USER)

        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(TWITTER_PASSWORD)

        password.send_keys(Keys.ENTER)

        sleep(5)
        enter_tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        enter_tweet.send_keys(tweet_text)

        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet.click()
        sleep(2)
        self.driver.quit()


speedbot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

speedbot.get_internet_speed()
print(f"Up:{speedbot.up} Down:{speedbot.down}")
tweet_text = f"Hey Internet Provider, why is my internet speed {speedbot.down}down/{speedbot.up}up when I pay for 150down/10up?"
speedbot.tweet_at_provider(tweet_text)

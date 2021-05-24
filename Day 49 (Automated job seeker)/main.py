from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException


chrome_driver_path = YOUR_DRIVER_PATH_HERE
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2563155224&f_AL=true&geoId=102713980&keywords=typist&location=India&sortBy=R")

sign_in = driver.find_element_by_link_text("Sign in")
sign_in.click()

time.sleep(5)

username = driver.find_element_by_id("username")
username.send_keys(YOUR_USERNAME_HERE)
password = driver.find_element_by_id("password")
password.send_keys(YOUR_PASSWORD_HERE)
password.send_keys(Keys.ENTER)

time.sleep(5)

search_results = driver.find_elements_by_class_name("job-card-list__title")



for result in search_results:
    result.click()
    time.sleep(5)
    try:
        apply = driver.find_element_by_class_name("jobs-apply-button")
        apply.click()
        try:
            contact_number = driver.find_element_by_class_name("fb-single-line-text__input")
            if contact_number.text == "":
                contact_number.send_keys(YOUR_CONTACT_NUMBER_HERE)

            submit = driver.find_element_by_css_selector('footer button')
            submit.click()
        except NoSuchElementException:
            pass
    except NoSuchElementException:
        pass



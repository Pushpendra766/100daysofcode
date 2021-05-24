from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = YOUR_DRIVER_PATH_HERE

driver = webdriver.Chrome(chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element_by_css_selector("#articlecount a")
# # article_count.click()
# all_portals = driver.find_element_by_link_text("All portals")
# # all_portals.click()
# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element_by_name("fName")
lname = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
fname.send_keys("my_first_name")
lname.send_keys("my_l_name")
email.send_keys("dasd@hmak.com")
button = driver.find_element_by_tag_name("button")
button.click()
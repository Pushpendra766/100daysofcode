from selenium import webdriver
chrome_driver_path = YOUR_DRIVER_PATH_HERE
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.in/Camel-Oil-Pastel-Reusable-Plastic/dp/B00LY12TH6/ref=sr_1_1?dchild=1&keywords=oil+pastels&qid=1621483789&sr=8-1")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)


driver.get("https://www.python.org/")

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

events_date = driver.find_elements_by_css_selector(".event-widget time")
events_name = driver.find_elements_by_css_selector(".event-widget li a")

events = {}
for i in range(len(events_date)):
    events[i] = {
        "date": events_date[i].text,
        "name": events_name[i].text
    }


print(events)
driver.quit()
# driver.close()

from selenium import webdriver
import time

chrome_driver_path = YOUR_DRIVER_PATH_HERE
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5

while True:
    cookie.click()

    if time.time() > timeout:
        items = driver.find_elements_by_css_selector("#store b")
        prices = []
        for item in items:
            element = item.text
            if element != "":
                price = int((element.split("- ")[1]).strip().replace(",", ""))
                prices.append(price)

        cookie_upgrades = {}
        for i in range(len(prices)):
            cookie_upgrades[prices[i]] = item_ids[i]

        money_element = (driver.find_element_by_id("money")).text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        affordable_upgrade = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrade[cost] = id

        highest_price_affordable_upgrade = max(affordable_upgrade)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrade[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookies_per_sec = driver.find_element_by_id("cps").text
        print(cookies_per_sec)
        break

driver.quit()

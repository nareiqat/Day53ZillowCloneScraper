from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

google_form = "create a google form and paste link here"
zillow_clone_link = "https://appbrewery.github.io/Zillow-Clone/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(zillow_clone_link)

zillow_property_prices = driver.find_elements(by=By.XPATH, value="//*[@id='zpid_2056905294']/div/div[1]/div[2]/div/span")

zillow_property_links = driver.find_elements(by=By.XPATH,
                                             value="//*[@id='zpid_2056905294']/div/div[2]/div[2]/a")
zillow_property_addresses = driver.find_elements(by=By.XPATH, value="//*[@id='zpid_2056905294']/div/div/a/address")

price = [price.text.split('+')[0].split('/')[0] for price in zillow_property_prices]
print(price)
link = [link.get_attribute("href") for link in zillow_property_links]
print(link)
address = [address.text.replace(" | ", "").strip() for address in zillow_property_addresses]
print(address)

for i in range(len(price)):
    driver.get(google_form)
    time.sleep(2)

    google_form_address = driver.find_element(by=By.XPATH,
                                              value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    google_form_price = driver.find_element(by=By.XPATH,
                                            value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    google_form_link = driver.find_element(by=By.XPATH,
                                           value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    submit_button = driver.find_element(by=By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    google_form_address.send_keys(address[i])
    google_form_price.send_keys(price[i])
    google_form_link.send_keys(link[i])
    submit_button.click()

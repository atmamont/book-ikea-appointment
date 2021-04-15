from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

ZIPCODE = ""
NAME = ""
PHONE = ""
EMAIL = ""

DRIVER_PATH = './chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
page = driver.get('https://planservice.ikea.nl/winkelafspraak')

# In the shop
shopButton = driver.find_elements_by_xpath("//div[contains(@data-option,'store')]")[0]
shopButton.click()


# Days of the week
dayOfWeeekButtons = driver.find_elements_by_xpath("//div[contains(@class,'selector-step selector-step-days')]//div[contains(@class,'option')]")
for button in dayOfWeeekButtons:
    button.click()


# Time of the day
timeOfTheDayButtons = driver.find_elements_by_xpath("//div[contains(@class,'selector-step selector-step-daypart')]//div[contains(@class,'option')]")
for button in timeOfTheDayButtons:
    button.click()


# Zip code
zipInput = driver.find_element_by_xpath("//input[contains(@class,'postalcode-input')]")
zipInput.send_keys(ZIPCODE+"\n")

sleep(2)

results = driver.find_elements_by_xpath("//div[contains(@class,'result-container')]//div[contains(@class,'item')]")
if len(results) == 0:
    exit()


print('Slot found!')
results[0].click()

sleep(2)


# Enter personal data
# Name
nameInput = driver.find_element_by_xpath("//input[contains(@name,'name')]")
nameInput.send_keys(NAME)

# Phone
phoneInput = driver.find_element_by_xpath("//input[contains(@name,'telephoneNumber')]")
phoneInput.send_keys(PHONE)

# Email
emailInput = driver.find_element_by_xpath("//input[contains(@name,'email')]")
emailInput.send_keys(EMAIL)

# Agreement
checkboxInput = driver.find_element_by_xpath("//input[contains(@type,'checkbox')]")
checkboxInput.click()

# Button
submitInput = driver.find_element_by_xpath("//div[contains(@class,'button blue submit')]")
submitInput.click()
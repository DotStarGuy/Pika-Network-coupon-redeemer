import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#word list
word1 = input("first word: ")
word2 = input("second word: ")
word3 = input("third word: ")

#User settings
username = "yourmMinecraftName"
name = username
mail = "yourmail"
region = "USA"
timer = 0.2 #For slower computers turn this up to 0.5
#the product is the direct link to what you want to purchase
product = "https://store.pika-network.net/checkout/packages/add/5414210/single"


# initializing browser
driver = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)





# creates every possible combination of the 3 given words
combination1 = word1 + "-" + word2 + "-" + word3
combination2 = word1 + "-" + word3 + "-" + word2
combination3 = word2 + "-" + word1 + "-" + word3
combination4 = word2 + "-" + word3 + "-" + word1
combination5 = word3 + "-" + word2 + "-" + word1
combination6 = word3 + "-" + word1 + "-" + word2

#Loging into the pika-network store
def login():
    driver.get("https://store.pika-network.net/login")
    print("starting_Driver")
    time.sleep(timer)
    Select_Box_Name = driver.find_element(by=By.NAME, value="ign")
    Select_Box_Name.click()
    time.sleep(timer)
    Select_Box_Name.send_keys(username)
    Select_Box_Name.click()
    time.sleep(timer)
    click_send = driver.find_element(by=By.CLASS_NAME, value="btn-lg")
    click_send.click()
    time.sleep(timer)
    buyKeys()

#Selects 5 winter keys and adds them to the cart and tries every single possible coupon combination
def buyKeys():
    driver.get(product)#The desired item
    time.sleep(timer)
    Select_Box_Name = driver.find_element(by=By.NAME, value="coupon")
    Select_Box_Name.click()
    time.sleep(timer)
    Select_Box_Name.send_keys(combination1)
    Select_Box_Name.click()
    time.sleep(timer)
    click_send = driver.find_element(by=By.CLASS_NAME, value="btn-primary")
    click_send.click()
    time.sleep(0.5)
    
    #Try with second combination
    Select_Box_Name = driver.find_element(by=By.NAME, value="coupon")
    Select_Box_Name.click()
    time.sleep(timer)
    Select_Box_Name.send_keys(combination2)
    Select_Box_Name.click()
    time.sleep(timer)
    click_send = driver.find_element(by=By.CLASS_NAME, value="btn-primary")
    click_send.click()
    time.sleep(0.5)
        #Try with third combination
    Select_Box_Name = driver.find_element(by=By.NAME, value="coupon")
    Select_Box_Name.click()
    time.sleep(timer)
    Select_Box_Name.send_keys(combination3)
    Select_Box_Name.click()
    time.sleep(timer)
    click_send = driver.find_element(by=By.CLASS_NAME, value="btn-primary")
    click_send.click()
    time.sleep(0.5)
        #Try with 4th combination
    Select_Box_Name = driver.find_element(by=By.NAME, value="coupon")
    Select_Box_Name.click()
    time.sleep(timer)
    Select_Box_Name.send_keys(combination4)
    Select_Box_Name.click()
    time.sleep(timer)
    click_send = driver.find_element(by=By.CLASS_NAME, value="btn-primary")
    click_send.click()
    time.sleep(0.5)
        #Try with 5th combination
    Select_Box_Name = driver.find_element(by=By.NAME, value="coupon")
    Select_Box_Name.click()
    time.sleep(timer)
    Select_Box_Name.send_keys(combination5)
    Select_Box_Name.click()
    time.sleep(timer)
    click_send = driver.find_element(by=By.CLASS_NAME, value="btn-primary")
    click_send.click()
    time.sleep(0.5)
        #Try with 6th combination
    Select_Box_Name = driver.find_element(by=By.NAME, value="coupon")
    Select_Box_Name.click()
    time.sleep(timer)
    Select_Box_Name.send_keys(combination6)
    Select_Box_Name.click()
    time.sleep(timer)
    click_send = driver.find_element(by=By.CLASS_NAME, value="btn-primary")
    click_send.click()
    time.sleep(0.5)
    personalInfo()

# fills out the personal information and leaves the user with selecting country and agreeing to terms
def personalInfo():
    Select_Box_Name = driver.find_element(by=By.NAME, value="address_name")
    Select_Box_Name.click()
    time.sleep(timer)
    Select_Box_Name.send_keys(name)
    Select_Box_Name.click()
    time.sleep(timer)
    Select_Box_Name = driver.find_element(by=By.NAME, value="email")
    Select_Box_Name.click()
    time.sleep(timer)
    Select_Box_Name.send_keys(mail)
    Select_Box_Name.click()
    time.sleep(timer)
    Select_Box_Name = driver.find_element(by=By.NAME, value="address_state")
    Select_Box_Name.click()
    time.sleep(timer)
    Select_Box_Name.send_keys(region)
    Select_Box_Name.click()
    time.sleep(timer)
    print("#####################################################################")
    print(combination1, combination2, combination3, combination4, combination5)
    print("#####################################################################")
    
login()

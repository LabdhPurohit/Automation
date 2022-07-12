import time

from selenium import webdriver
from selenium.webdriver.common.by import By

d=webdriver.Chrome(executable_path='C:\chromedriver.exe')

d.get('https://www.saucedemo.com/')
d.maximize_window()

username =d.find_element_by_xpath('//*[@id="user-name"]')
username.click()
username.send_keys('standard_user')


password =d.find_element_by_xpath('//*[@id="password"]')
password.click()
password.send_keys('secret_sauce')

login =d.find_element_by_xpath('//*[@id="login-button"]')
login.click()

addToCart1 =d.find_element_by_xpath('//*[@id="add-to-cart-sauce-labs-backpack"]')
addToCart1.click()

addToCart2 =d.find_element_by_xpath('//*[@id="add-to-cart-sauce-labs-bike-light"]')
addToCart2.click()

addToCart3 =d.find_element_by_xpath('//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
addToCart3.click()

Cart =d.find_element_by_xpath('//*[@id="shopping_cart_container"]/a')
Cart.click()

Checkout =d.find_element_by_xpath('//*[@id="checkout"]')
Checkout.click()

fn =d.find_element_by_xpath('//*[@id="first-name"]')
fn.click()
fn.send_keys('XY')

ln =d.find_element_by_xpath('//*[@id="last-name"]')
ln.click()
ln.send_keys('Z')

PostalArea =d.find_element_by_xpath('//*[@id="postal-code"]')
PostalArea.click()
PostalArea.send_keys('12345')

Continue=d.find_element_by_xpath('//*[@id="continue"]')
Continue.click()

Payment=d.find_element_by_xpath('//*[@id="finish"]')
Payment.click()

time.sleep(200)
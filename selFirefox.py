from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pynput.keyboard import Key, Controller
import os

driver = webdriver.Firefox()
keyboard = Controller()

time.sleep(5)

myUsername = os.environ.get('username_7mar')
myPassword = os.environ.get('password_7mar')

driver.refresh()

driver.get("https://instagram.com")

time.sleep(5)

username = driver.find_element_by_name("username")
username.send_keys(myUsername)

time.sleep(2)

password = driver.find_element_by_name("password")
password.send_keys(myPassword)

time.sleep(5)

LOG = driver.find_element_by_class_name("Igw0E")
LOG.click()

time.sleep(5)

notNow1 = driver.find_element_by_class_name("y3zKF")
notNow1.click()
print("not now1")

time.sleep(5)

notNow2 = driver.find_element_by_class_name("HoLwm")
notNow2.click()
print("not now2")

time.sleep(5)

keyboard.press(Key.ctrl)
keyboard.press(Key.shift)
keyboard.press('i')
keyboard.release(Key.shift)
keyboard.release(Key.ctrl)
keyboard.release('i')

print("iiiiiiiiiiiiiiiii")
time.sleep(5)

keyboard.press(Key.ctrl)
keyboard.press(Key.shift)
keyboard.press('m')
keyboard.release(Key.shift)
keyboard.release(Key.ctrl)
keyboard.release('m')

print("mmmmmmmmmmm")
time.sleep(5)

driver.refresh()
print("xxxxxxxxxx refresh")

time.sleep(5)

cancel = driver.find_element_by_class_name("HoLwm")
cancel.click()
print("cancel")

time.sleep(10)

driver.find_element_by_class_name("_8-yf5").send_keys("C://Users/Windows 10 Pro/Desktop/7mar/photos/photo1.jpg")

time.sleep(500)

driver.close()
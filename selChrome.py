from selenium import webdriver
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException 
import time
import os

keyboard = Controller()
chrome_options = Options()
driver = webdriver.Chrome(executable_path="C:\\Users\\Windows 10 Pro\\Desktop\\DDownloads\\chromedriver.exe")

driver.get("https://instagram.com")

myUsername = os.environ.get('username_7mar')
myPassword = os.environ.get('password_7mar')
time.sleep(2)

username = driver.find_element_by_name("username")
username.send_keys(myUsername)
print("username")

time.sleep(1)

password = driver.find_element_by_name("password")
password.send_keys(myPassword)
print("password")

time.sleep(2)

LOG = driver.find_element_by_class_name("Igw0E")
LOG.click()
print("long in")
time.sleep(3)

notNow1 = driver.find_element_by_class_name("y3zKF")
notNow1.click()
print("not now1")

time.sleep(3)

notNow2 = driver.find_element_by_class_name("HoLwm")
notNow2.click()
print("not now2")

time.sleep(3)

keyboard.press(Key.ctrl)
keyboard.press(Key.shift)
keyboard.press('i')
keyboard.release(Key.shift)
keyboard.release(Key.ctrl)
keyboard.release('i')

print("iiiiiiiiiiiiiiiii")
time.sleep(2)

keyboard.press(Key.ctrl)
keyboard.press(Key.shift)
keyboard.press('m')
keyboard.release(Key.shift)
keyboard.release(Key.ctrl)
keyboard.release('m')

print("mmmmmmmmmmm")
time.sleep(2)

driver.refresh()
print("xxxxxxxxxx refresh")

time.sleep(5)

keyboard.press(Key.ctrl)
keyboard.press(Key.shift)
keyboard.press('m')
keyboard.release(Key.shift)
keyboard.release(Key.ctrl)
keyboard.release('m')

time.sleep(5)

try:
    cancel = driver.find_element_by_class_name("HoLwm")
    cancel.click()
except NoSuchElementException as e:
    print("shit")

print("cancel")

time.sleep(3)
keyboard.press(Key.ctrl)
keyboard.press(Key.shift)
keyboard.press('i')
keyboard.release(Key.shift)
keyboard.release(Key.ctrl)
keyboard.release('i')


actions = ActionChains(driver)
element = driver.find_element_by_class_name("_8-yf5")
actions.move_to_element(element)
actions.click()
actions.send_keys("C://Users/Windows 10 Pro/Desktop/7mar/photos/photo1.jpg")
actions.perform()
time.sleep(1)

# button = driver.find_element_by_class_name("cB_4K")
# actions.move_to_element(button).click(button).perform()


print("done")
time.sleep(500)

driver.close()
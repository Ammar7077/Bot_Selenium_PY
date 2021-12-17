from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pynput.keyboard import Key, Controller
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
keyboard = Controller()

time.sleep(0)

myUsername = os.environ.get('username_7mar')
myPassword = os.environ.get('password_7mar')

driver.refresh()

driver.get("https://instagram.com")

time.sleep(1)

username = driver.find_element_by_name("username")
username.send_keys(myUsername)

time.sleep(1)

password = driver.find_element_by_name("password")
password.send_keys(myPassword)

time.sleep(1)

LOG = driver.find_element_by_class_name("Igw0E")
LOG.click()

time.sleep(8)
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".sqdOP.yWX7d.y3zKF"))).click()

# sqdOP.yWX7d.y3zKF not now
# notNow1 = driver.find_element_by_class_name("yWX7d")
# notNow1.click()
print("not now1")

time.sleep(6)

WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".aOOlW.HoLwm"))).click()

print("notNow2.click()")

time.sleep(2)

# keyboard.press(Key.ctrl)
# keyboard.press(Key.shift)
# keyboard.press('i')
# keyboard.release(Key.shift)
# keyboard.release(Key.ctrl)
# keyboard.release('i')

# print("iiiiiiiiiiiiiiiii")
# time.sleep(5)

# keyboard.press(Key.ctrl)
# keyboard.press(Key.shift)
# keyboard.press('m')
# keyboard.release(Key.shift)
# keyboard.release(Key.ctrl)
# keyboard.release('m')

# print("mmmmmmmmmmm")
# time.sleep(5)

# driver.refresh()
# print("xxxxxxxxxx refresh")








# WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".qF0y9.Igw0E.rBNOH.eGOV_.ybXk5._4EzTm.XfCBB.HVWg4.La5L3.ZUqME"))).click()
# time.sleep(2)
# driver.find_element_by_id("f2f460b2a751d36").click()

WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".wpO6b.ZQScA"))).click()
print("Add post click")
# WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[./span[text()='Not Now']]"))).click()

time.sleep(2)
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.zQLcH.XTCZH"))).click()
# driver.find_element_by_class_name(".qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.zQLcH.XTCZH").send_keys(os.getcwd()+"C://Users/Windows 10 Pro/Desktop/7mar/photos/photo1.jpg")

#Btn Next->Next->Share#     qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.XfCBB.g6RW6
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.XfCBB.g6RW6"))).click()

time.sleep(1)
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.XfCBB.g6RW6"))).click()

time.sleep(1)
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.XfCBB.g6RW6"))).click()


# f2f460b2a751d36
# qF0y9.Igw0E.rBNOH.eGOV_.ybXk5._4EzTm.XfCBB.HVWg4.La5L3.ZUqME


time.sleep(1000)

driver.close()
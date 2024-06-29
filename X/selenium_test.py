import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_PIN(url):
    driver = webdriver.Chrome()

    driver.get(url)

    user_name_bar = driver.find_element(By.XPATH, '/html/body/div[2]/div/form/fieldset[1]/div[1]/input')

    user_name_bar.send_keys("YOUR-X-ACCOUNT")

    password_bar = driver.find_element(By.XPATH, '/html/body/div[2]/div/form/fieldset[1]/div[2]/input')

    password_bar.send_keys("YOUR-X-PASSWORD")

    password_bar.submit()

    PIN = driver.find_element(By.XPATH, '/html/body/div[2]/div/p/kbd/code')

    return PIN.text

import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

def news_titles():
    driver = webdriver.Chrome()

    driver.get('https://udn.com/news/breaknews')

    current_time = datetime.now().strftime("%p %I:%M:%S")

    titles = "聯合新聞網至 " + current_time + " 為止的重要新聞:" + "\n\n"

    for i in range (1,4):
        title = driver.find_element(By.XPATH, '/html/body/main/div/section[2]/section/div[1]/div[' + str(i) + ']/div[2]/h2/a')
        titles = titles + "No." + str(i) + " - " + title.text + '\n\n'
    return titles
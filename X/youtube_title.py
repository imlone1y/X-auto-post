import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

def youtube_titles():
    driver = webdriver.Chrome()

    driver.get('https://www.youtube.com/feed/trending')

    current_time = datetime.now().strftime("%p %I:%M:%S")

    titles = "youtube 至 " + current_time + " 為止的發燒影片為:" + "\n\n"
    
    for i in range (1,4):
        title = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-shelf-renderer/div[1]/div[2]/ytd-expanded-shelf-contents-renderer/div/ytd-video-renderer['+ str(i) +']/div[1]/div/div[1]/div/h3/a/yt-formatted-string')
        titles = titles + "No." + str(i) + " - " + title.text + '\n\n'

    return titles

# Import External Libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import datetime

# Congigure Options
chrome_options = webdriver.ChromeOptions(); 
# chrome_options.add_argument("--headless") # runs in background
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']); # hide info bar

# Create Driver
driver = webdriver.Chrome(options=chrome_options)

# Get Website
driver.get('https://www.youtube.com/c/FlyingDoodles/videos?view=0&sort=dd&flow=grid')

# find videos
nodes = driver.find_elements(By.CLASS_NAME , 'style-scope ytd-grid-video-renderer')
videos = []
for node in nodes:
    title = node.find_element(By.ID, 'video-title').text
    views = node.find_element(By.XPATH, './/*[@id="metadata-line"]/span[1]').text
    videos.append({'title': title, 'views': views})

df = pd.DataFrame(videos)
print(df)

df.to_csv('video_records/' + str(datetime.now()) + '.csv', index = False)
# driver.close()

# run periodicly -> windows: Task Scheduler Wizard, mac: crontab terminal command
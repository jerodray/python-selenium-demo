# Import External Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By

# Congigure Options to hide info bar
chrome_options = webdriver.ChromeOptions();
# chrome_options.add_argument("--headless") # runs in background
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);

# Create Driver
driver = webdriver.Chrome(options=chrome_options);  

# Get Website
driver.get('https://google.com')

# make inputs
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('infiniti g35')
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()

result_count = driver.find_element(By.XPATH, '//*[@id="result-stats"]').text

print(result_count)

# driver.close()



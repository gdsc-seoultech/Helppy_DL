from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
import os

keyword = str(input("insert keyword for searching : "))
path = os.path.join('./crawling/data/', keyword)
if not os.path.exists(path):
    os.makedirs(path)

driver = webdriver.Chrome(executable_path = r'./chromedriver') 
driver.get("https://www.google.co.kr/imghp?hl=ko&authuser=0&ogbl")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input.gLFyf").send_keys(keyword) 
driver.find_element(By.CSS_SELECTOR,"input.gLFyf").send_keys(Keys.RETURN)


last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try: break
        except : break
    last_height = new_height
i=1
imgs = driver.find_elements(By.CSS_SELECTOR,"img.rg_i.Q4LuWd")
address = (f'./crawling/data/{keyword}')
print(len(imgs))
for img in imgs:
    try:
        print(i)
        if i == 101:
            break
        imgurl = img.get_attribute("src")
        time.sleep(1)
        urllib.request.urlretrieve(imgurl,address+"/"+str(keyword)+str(i)+".jpeg")
        i += 1
    except:
        pass
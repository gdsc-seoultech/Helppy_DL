from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
import os

driver = webdriver.Chrome(executable_path = r'/nas/home/drizzle0171/Solution-Challenge-2023/Image-captioning/crawling/chromedriver') 

keyword = str(input("insert keyword for searching : "))
path = os.path.join(keword)
if not os.path.exists(path):
    os.makedirs(path)

driver.get("https://www.google.co.kr/imghp?hl=ko&authuser=0&ogbl")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_css_selector("input.gLFyf").send_keys(keyword) 
driver.find_element_by_css_selector("input.gLFyf").send_keys(Keys.RETURN)


last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

i=0

list = driver.find_elements_by_css_selector("img.rg_i.Q4LuWd")
print(len(list))


address = (f'./{keyword}')
for img in list:
    i += 1
    try:

        imgurl = img.get_attribute("src")
        time.sleep(1)
        urllib.request.urlretrieve(imgurl,address+"/"+str(keyword)+str(i)+".jpeg")

    except:
        pass
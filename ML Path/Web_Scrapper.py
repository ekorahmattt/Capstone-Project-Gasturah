#from turtle import done

from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image

import requests
import io
import time

PATH = "C:\\Users\\erdar\\Desktop\\ML Path\\Web Scrapping\\chromedriver.exe"    

# Get Image From Google Image Function
def get_images(wd, delay, max_img, url):
    
    def scroll_down(wd):
    
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)
    
    wd.get(url)
    img_targets = set()
    skips = 0
    
    while len(img_targets) + skips < max_img:
        scroll_down(wd)
        
        thumb = wd.find_elements(By.CLASS_NAME, "Q4LuWd")
        
        for img in thumb[len(img_targets) + skips:max_img]:
            try:
                img.click()
                time.sleep(delay)
            except:
                continue
            
            images = wd.find_elements(By.CLASS_NAME, "n3VNCb")
            
            for image in images:
                if image.get_attribute('src') in img_targets:
                    max_img += 1
                    skips += 1
                    break
                
                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    img_targets.add(image.get_attribute('src'))
                    print("Image {} founded".format(len(img_targets)))
                    
    return img_targets
        
# Download image function
def download_images(url, download_path, file_name):
    
    try:
        img_content = requests.get(url).content
        img_file = io.BytesIO(img_content)
        image = Image.open(img_file)
        file_path = download_path + file_name
        
        with open(file_path, 'wb') as img:
            image.save(img, "JPEG")
        print("Download Succes!")
    
    except Exception as e:
        print("Failed : ", e)

#____________________________________________________
# Put your target url / Link google image which your select   
url = "https://www.google.com/search?q=monas&tbm=isch&ved=2ahUKEwjJwc3khtf3AhWNGbcAHZvqBHAQ2-cCegQIABAA&oq=monas&gs_lcp=CgNpbWcQAzIHCAAQsQMQQzIHCAAQsQMQQzILCAAQgAQQsQMQgwEyCAgAEIAEELEDMggIABCxAxCDATIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIICAAQgAQQsQMyCwgAEIAEELEDEIMBOgcIIxDvAxAnOgQIABBDOgQIABADOgoIABCxAxCDARBDUJ4FWLoIYIkRaABwAHgAgAG9CIgBiRaSAQU2LTIuMZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=AHd7YsnBHo2z3LUPm9WTgAc"

wd = webdriver.Chrome(PATH)

data = get_images(wd, 1, 10, url) # 10 is max_images will downloaded, you can modified how many you want 

for i, pict in enumerate(data):
    # You should create a folder before you download images in same folder
    download_images(pict, "Monas/", str(i) +".jpg") # Monas/ is folder name

wd.quit()
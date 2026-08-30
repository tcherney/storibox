

import sys
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


if __name__ == "__main__":
    url = sys.argv[1]
    driver = webdriver.Chrome()
    driver.get(url)
    sleep(5)  # Wait for the page to load
    images = driver.find_elements(By.CSS_SELECTOR, "img.gallery__item-img")
    current_index = 0
    for img in images:
        if 'src' in img.get_attribute("outerHTML"):
            print(f"Image {current_index}: {img.get_attribute('src')}")
            img_url = img.get_attribute('src')
            if img_url.endswith('.jpg') or img_url.endswith('.jpeg'):
                response = requests.get(img_url)
                if response.status_code == 200:
                    with open(f'image_{current_index}.jpg', 'wb') as f:
                        f.write(response.content)
                    current_index += 1
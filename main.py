

import sys
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


if __name__ == "__main__":
    url = sys.argv[1]
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options) # Use headless mode for Chrome
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
    view_button = driver.find_element(By.CSS_SELECTOR, "img.gallery__item-view")
    view_button.click()
    sleep(1)
    videos = driver.find_elements(By.CSS_SELECTOR, "video.full-screen-view__content")
    print(f"Found {len(videos)} videos on the page.")
    current_index = 0
    for video in videos:
        source = video.find_element(By.TAG_NAME, "source")
        print(f"Video {current_index}: {source.get_attribute('src')}",source)
        if 'src' in source.get_attribute("outerHTML"):
            print(f"Video {current_index}: {source.get_attribute('src')}")
            video_url = source.get_attribute('src')
            if video_url.endswith('.mp4'):
                response = requests.get(video_url)
                if response.status_code == 200:
                    with open(f'video_{current_index}.mp4', 'wb') as f:
                        f.write(response.content)
                    current_index += 1
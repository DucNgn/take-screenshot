#!/usr/bin/python

import sys
import hashlib
import time
import config

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def store_image(driver):
    hash = hashlib.sha1()
    hash.update(str(time.time()).encode("utf-8"))
    filename = hash.hexdigest()[:8]
    file_location = config.SCREENSHOT_DIR / f"{filename}.png"
    return driver.save_screenshot(str(file_location)), f"{filename}.png"

def main():
    for url in sys.argv:
        if url  == "take_screenshot.py":
            continue

        print(f'Taking Screenshot of URL: {url}')
        chrome_driver = ChromeDriverManager(log_level=0).install()
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--disable-dev-shm-usage')        
        chrome_options.add_argument("--headless")

        # Get the height of the URL.
        driver = webdriver.Chrome(chrome_driver, options=chrome_options)
        driver.get(url)
        time.sleep(3)
        height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight )")
        driver.close()

        # Start another headless browser with the extracted height.
        chrome_options.add_argument(f"--window-size=1920,{height}")
        chrome_options.add_argument("--hide-scrollbars")
        driver = webdriver.Chrome(chrome_driver, options=chrome_options)
        driver.get(url)
        time.sleep(3)

        success, filename = store_image(driver)
        if success:
            print(f"Successful! Screenshot saved as {filename}.")
        else:
            print("Failed to take screenshot.")

        driver.close()

if __name__ == "__main__":
    main()


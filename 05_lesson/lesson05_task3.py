import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


# Запуск браузера с автоматической установкой совместимого драйвера
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
# Пример: откроем сайт
driver.get("https://the-internet.herokuapp.com/inputs")
search_box = driver.find_element(By.XPATH, '//input[@type="number"]')
search_box.send_keys("Sky")
time.sleep(5)
search_box.clear()
search_box.send_keys("Pro")
time.sleep(5)

driver.quit()

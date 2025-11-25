from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()

    browser.get(link)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()
    
    tabs = browser.window_handles
    browser.switch_to.window(tabs[1])

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    
    result = math.log(abs(12 * math.sin(x)))
    
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(str(result))
    
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()
    
    time.sleep(2)
    alert = browser.switch_to.alert
    answer_text = alert.text
    print("Полученный ответ:", answer_text)
    
finally:
    time.sleep(2)
    browser.quit()
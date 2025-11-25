from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()

    browser.get(link)
    
    price_wait = WebDriverWait(browser, 15)
    price_wait.until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)

    result = math.log(abs(12 * math.sin(x)))

    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(str(result))

    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()
    
    time.sleep(2)
    alert = browser.switch_to.alert
    answer_text = alert.text
    print("Полученный ответ:", answer_text)
    
finally:
    time.sleep(8)
    browser.quit()
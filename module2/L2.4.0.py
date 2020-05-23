from selenium import webdriver
import time
import os
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    # browser.get("http://suninjuly.github.io/wait1.html")
    # browser.get("http://suninjuly.github.io/cats.html")
    browser.get("http://suninjuly.github.io/wait2.html")

    # button = browser.find_element_by_id("verify")
    button = browser.find_element_by_id("verify")
    button.click()

    message = browser.find_element_by_id("verify_message")
    print(message.text)
    assert "successful" in message.text
    print(message.text)

except Exception as e:  # Отлавливаем все ошибки в коде или просто "except:"
    print(type(e))
    print(e)
    print(e.args)


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

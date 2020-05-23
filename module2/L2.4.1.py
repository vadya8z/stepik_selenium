from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )

    #print(price)

    button = browser.find_element_by_id("book")
    button.click()


    x = WebDriverWait(browser, 12).until(
        EC.presence_of_element_located((By.ID, "input_value"))
    )
    #print(x.text)
    y = calc(x.text)
    input_out = browser.find_element_by_id('answer')
    input_out.send_keys(y)

    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()

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

#https://stepik.org/lesson/184253/step/4?unit=158843
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector('button[type="submit"]').click()
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)

    x = browser.find_element_by_id('input_value').text
    y = calc(x)
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
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

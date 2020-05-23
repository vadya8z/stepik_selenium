#https://stepik.org/lesson/165493/step/5?unit=140087
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math


# link = "http://suninjuly.github.io/selects1.html"
link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('num1').text
    y = browser.find_element_by_id('num2').text
    s = str(int(x)+int(y))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(s)  # ищем элемент с текстом cуммы значений

    # browser.find_element_by_tag_name("select").click()
    # browser.find_element_by_css_selector("option:nth-child(2)").click()
    # browser.find_element_by_css_selector("[value='1']").click()

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

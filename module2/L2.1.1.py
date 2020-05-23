#https://stepik.org/lesson/165493/step/5?unit=140087
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input_out = browser.find_element_by_id('answer')
    input_out.send_keys(y)

    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()

    # people_radio = browser.find_element_by_id("peopleRule")
    # people_checked = people_radio.get_attribute("checked")
    # print("value of people radio: ", people_checked)
    # assert people_checked is not None, "People radio is not selected by default"
    # assert people_checked == "true", "People radio is not selected by default"
    #
    # robots_radio = browser.find_element_by_id("robotsRule")
    # robots_checked = robots_radio.get_attribute("checked")
    # assert robots_checked is None, 'robotsRule is not selected by default'

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

#https://stepik.org/lesson/228249/step/8?unit=200781
from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector('input[name="firstname"]').send_keys('Fname')
    browser.find_element_by_css_selector('input[name="lastname"]').send_keys('Lname')
    browser.find_element_by_css_selector('input[name="email"]').send_keys('a@a.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

    browser.find_element_by_css_selector('input[type="file"]').send_keys(file_path)


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

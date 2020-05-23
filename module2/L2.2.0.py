# from selenium import webdriver
# import time
#
#
# try:
#     browser = webdriver.Chrome()
#     # browser.execute_script("document.title='Script executing';")
#     # browser.execute_script("alert('Robots at work');")
#     # browser.execute_script("document.title='Script executing';alert('Robots at work');")
#
#     link = "https://SunInJuly.github.io/execute_script.html"
#     browser.get(link)
#     button = browser.find_element_by_tag_name("button")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button) #Скролл к заданному элементу страницы что бы он был виден https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView
#     browser.execute_script("window.scrollBy(0, 100);") # Скролл на 100px
#     button.click()
#     assert True
#
# except Exception as e:  # Отлавливаем все ошибки в коде или просто "except:"
#     print(type(e))
#     print(e)
#     print(e.args)
#
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(15)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла


import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
#element.send_keys(file_path) - элемент выбранный через вебдрайвер
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
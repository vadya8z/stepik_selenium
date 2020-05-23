from selenium import webdriver
import time
import os


try:
    browser = webdriver.Chrome()
    #js Alert
    alert = browser.switch_to.alert
    alert.accept()
    alert_text = alert.text
    #js Confirm
    confirm = browser.switch_to.alert
    confirm.accept()
    confirm.dismiss()
    #js Prompt
    prompt = browser.switch_to.alert
    prompt.send_keys("My answer")
    prompt.accept()
    #Переход на новую вкладку браузера
    #browser.switch_to.window(window_name)
    # new_window = browser.window_handles[1] #Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку
    # first_window = browser.window_handles[0] #Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться


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

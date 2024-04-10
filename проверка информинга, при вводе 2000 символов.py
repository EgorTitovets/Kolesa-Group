
#проверка информинга, при вводе 2000 символов.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://avtoelon.uz"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем "Поставить объявление"
    place_an_ad = browser.find_element(By.XPATH, "//a[@href='/a/new/']")
    place_an_ad.click()


    # Выбираем категорию "Машины"
    category_cars = browser.find_element(By.XPATH, "//select[@id='change-section-select']/option[1]")
    category_cars.click()
    time.sleep(1)

    # Выбираем подкатегорию "Легковые"
    auto_car = browser.find_element(By.XPATH, "//select[@id='change-category-select']/option[text()='Легковые']")
    auto_car.click()
    time.sleep(1)

    # Находим поле для ввода дополнительной информации и вводим в него 2000 символов
    additional_information_2000 = browser.find_element(By.XPATH, "//textarea[ @ id = 'text']")
    text_2000_symbols = 'a' * 2000
    additional_information_2000.send_keys(text_2000_symbols)
    time.sleep(2)

    # Находим элемент с сообщением об ошибке
    error_message = browser.find_element(By.XPATH, "// div[contains(@class , 'input-info')] /span[@class ='total-symbols']")
    displayed_error_message = error_message.text

    expected_error_message = "Максимальная длина текста  2000 знаков. Осталось 0 знаков."

    # Сравниваем отображаемый информинг с ожидаемым
    if displayed_error_message.replace(' ', '') == expected_error_message.replace(' ', ''):
        print(f"Отображаемый информинг '{displayed_error_message}' соответствует ожидаемому информингу '{expected_error_message}'")
        print("Тест выполнен успешно.")
    else:
        print(f"Ошибка. Отображаемый информинг '{displayed_error_message}' не соответствует ожидаемому информинг '{expected_error_message}'")
        print("ERROR")


finally:
    browser.quit()


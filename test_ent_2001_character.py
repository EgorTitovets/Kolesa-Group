#проверка невозможности ввода 2001 символа

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
def test_check_max_input(browser):
    link = "https://avtoelon.uz"
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

    # Находим поле для ввода дополнительной информации и вводим в него 2001 символ
    additional_information_2001 = browser.find_element(By.XPATH, "//textarea[@id='text']")
    text_2001_symbols = 'a' * 2001
    additional_information_2001.send_keys(text_2001_symbols)
    time.sleep(3)

    input_value = additional_information_2001.get_attribute("value")

    # Проверяем длину введенного текста
    assert len(input_value) == 2000, "Ошибка: Ввод не был обрезан до 2000 символов."

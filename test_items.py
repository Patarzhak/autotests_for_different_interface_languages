import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_items(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    add_to_basket_button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(add_to_basket_button) > 0, "Кнопка добавления в корзину не найдена"

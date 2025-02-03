import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from myuser import User
from locators import TestLocators

def test_click_on_logout_button_to_logout_success(driver):
    email = User.email
    password = User.password
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(*TestLocators.login_email).send_keys(email)
    driver.find_element(*TestLocators.login_password).send_keys(password)
    driver.find_element(*TestLocators.login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.order_button)))
    driver.find_element(*TestLocators.personal_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.save_button)))
    driver.find_element(*TestLocators.logout_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.login_button)))
    assert driver.find_element(*TestLocators.register_button_on_login_page).text == 'Зарегистрироваться'
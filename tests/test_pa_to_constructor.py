import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from myuser import User
from locators import TestLocators

def test_click_on_constructor_to_constructor_success(driver):
    email = User.email
    password = User.password
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(*TestLocators.login_email).send_keys(email)
    driver.find_element(*TestLocators.login_password).send_keys(password)
    driver.find_element(*TestLocators.login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.order_button)))
    driver.find_element(*TestLocators.personal_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.save_button)))
    driver.find_element(*TestLocators.constructor_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.order_button)))
    assert driver.find_element(*TestLocators.constructor_burger_h1).text == 'Соберите бургер'

def test_click_on_logo_to_constructor_success(driver):
    email = User.email
    password = User.password
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(*TestLocators.login_email).send_keys(email)
    driver.find_element(*TestLocators.login_password).send_keys(password)
    driver.find_element(*TestLocators.login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.order_button)))
    driver.find_element(*TestLocators.personal_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.save_button)))
    driver.find_element(*TestLocators.logo_burgers).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.order_button)))
    assert driver.find_element(*TestLocators.constructor_burger_h1).text == 'Соберите бургер'
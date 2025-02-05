import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from myuser import User
from locators import TestLocators
from urls import URLs



def test_constructor_click_sauce_button_success(driver):
    main = URLs.main
    email = User.email
    password = User.password
    driver.get(main)
    driver.find_element(*TestLocators.login_button_on_main_page).click()
    driver.find_element(*TestLocators.login_email).send_keys(email)
    driver.find_element(*TestLocators.login_password).send_keys(password)
    driver.find_element(*TestLocators.login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.order_button)))
    driver.find_element(*TestLocators.sauce_button).click()
    assert driver.find_element(*TestLocators.sauce_button).text == 'Соусы'

def test_constructor_click_bun_button_success(driver):
    main = URLs.main
    email = User.email
    password = User.password
    driver.get(main)
    driver.find_element(*TestLocators.login_button_on_main_page).click()
    driver.find_element(*TestLocators.login_email).send_keys(email)
    driver.find_element(*TestLocators.login_password).send_keys(password)
    driver.find_element(*TestLocators.login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.order_button)))
    driver.find_element(*TestLocators.sauce_button).click()
    driver.find_element(*TestLocators.bun_button).click()
    assert driver.find_element(*TestLocators.bun_button).text == 'Булки'

def test_constructor_click_filling_button_success(driver):
    main = URLs.main
    email = User.email
    password = User.password
    driver.get(main)
    driver.find_element(*TestLocators.login_button_on_main_page).click()
    driver.find_element(*TestLocators.login_email).send_keys(email)
    driver.find_element(*TestLocators.login_password).send_keys(password)
    driver.find_element(*TestLocators.login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.order_button)))
    driver.find_element(*TestLocators.filling_button).click()
    assert driver.find_element(*TestLocators.filling_button).text == 'Начинки'
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from myuser import User
from locators import TestLocators
from urls import URLs



def test_login_on_main_page_valid_data_success(driver):
    main = URLs.main
    email = User.email
    password = User.password
    driver.get(main)
    driver.find_element(*TestLocators.login_button_on_main_page).click()
    driver.find_element(*TestLocators.login_email).send_keys(email)
    driver.find_element(*TestLocators.login_password).send_keys(password)
    driver.find_element(*TestLocators.login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.order_button)))
    driver.find_element(*TestLocators.personal_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.save_button)))
    assert driver.find_element(*TestLocators.profile_button).get_attribute('aria-current') == 'page'

def test_login_on_personal_account_button_valid_data_success(driver):
    main = URLs.main
    email = User.email
    password = User.password
    driver.get(main)
    driver.find_element(*TestLocators.personal_account_button).click()
    WebDriverWait(driver, 3)
    driver.find_element(*TestLocators.login_email).send_keys(email)
    driver.find_element(*TestLocators.login_password).send_keys(password)
    driver.find_element(*TestLocators.login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.order_button)))
    driver.find_element(*TestLocators.personal_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.save_button)))
    assert driver.find_element(*TestLocators.profile_button).get_attribute('aria-current') == 'page'

def test_login_on_registration_page_valid_data_success(driver):
    register = URLs.register
    email = User.email
    password = User.password
    driver.get(register)
    driver.find_element(*TestLocators.login_button_on_registration_page).click()
    WebDriverWait(driver, 3)
    driver.find_element(*TestLocators.login_email).send_keys(email)
    driver.find_element(*TestLocators.login_password).send_keys(password)
    driver.find_element(*TestLocators.login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.order_button)))
    driver.find_element(*TestLocators.personal_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.save_button)))
    assert driver.find_element(*TestLocators.profile_button).get_attribute('aria-current') == 'page'

def test_login_on_forgot_button_page_valid_data_success(driver):
    forgot_password = URLs.forgot_password
    email = User.email
    password = User.password
    driver.get(forgot_password)
    driver.find_element(*TestLocators.login_button_on_registration_page).click()
    WebDriverWait(driver, 3)
    driver.find_element(*TestLocators.login_email).send_keys(email)
    driver.find_element(*TestLocators.login_password).send_keys(password)
    driver.find_element(*TestLocators.login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.order_button)))
    driver.find_element(*TestLocators.personal_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.save_button)))
    assert driver.find_element(*TestLocators.profile_button).get_attribute('aria-current') == 'page'
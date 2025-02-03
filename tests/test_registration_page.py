import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import generator
from locators import TestLocators

def test_registration_valid_data_success(driver):
    username = generator.username
    email = generator.email
    password = generator.password
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*TestLocators.name).send_keys(username)
    driver.find_element(*TestLocators.email).send_keys(email)
    driver.find_element(*TestLocators.password).send_keys(password)
    driver.find_element(*TestLocators.register_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.recovery_password_button)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

def test_registration_no_name_failed(driver):
    email = generator.email
    password = generator.password
    empty = ''
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*TestLocators.name).send_keys(empty)
    driver.find_element(*TestLocators.email).send_keys(email)
    driver.find_element(*TestLocators.password).send_keys(password)
    driver.find_element(*TestLocators.register_button).click()
    WebDriverWait(driver, 3)
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

def test_registration_incorrect_email_failed(driver):
    username = generator.username
    incorrect_email = generator.incorrect_email
    password = generator.password
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*TestLocators.name).send_keys(username)
    driver.find_element(*TestLocators.email).send_keys(incorrect_email)
    driver.find_element(*TestLocators.password).send_keys(password)
    driver.find_element(*TestLocators.register_button).click()
    WebDriverWait(driver, 3)
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

def test_registration_incorrect_password_failed(driver):
    username = generator.username
    email = generator.email
    incorrect_password = generator.incorrect_password
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*TestLocators.name).send_keys(username)
    driver.find_element(*TestLocators.email).send_keys(email)
    driver.find_element(*TestLocators.password).send_keys(incorrect_password)
    driver.find_element(*TestLocators.register_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.incorrect_password_alert)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'
# -*- coding: utf-8 -*-
from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

from contact import Contact

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="/Users/zafar/Documents/GitHub/libs/geckodriver")
        self.driver.implicitly_wait(30)
    
    def test_add_contact(self):
        driver = self.driver
        self.login(driver, username="admin", password="secret")
        self.create_contact(driver,  Contact (first_name = "JOKhan", last_name="Whitwad", mobile_number="3919999992", email="adaiy@company.com"))

    def test_add_empty_contact(self):
        driver = self.driver
        self.login(driver, username="admin", password="secret")
        self.create_contact(driver,Contact (first_name="", last_name="", mobile_number="", email="x@y.com"))

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()
        self.logout(driver)

    def return_to_home_page(self, driver):
        driver.find_element_by_link_text("home").click()

    def create_contact(self, driver, contact):
        # init contact creation
        driver.find_element_by_link_text("add new").click()
        # fill contact form
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.first_name)
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.last_name)
        driver.find_element_by_name("home").click()
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(contact.mobile_number)
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(contact.email)
        # submit contact creation
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()
        self.return_to_home_page(driver)

    def login(self, driver, username, password):
        self.open_home_page(driver)
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]").click()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

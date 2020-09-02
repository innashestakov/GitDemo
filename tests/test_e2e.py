import time

import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.checkout_page import CheckoutPage
from page_objects.confirm_page import ConfirmPage
from page_objects.home_page import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.get_logger()

# First page - home page

        home_page = HomePage(self.driver)
        home_page.shop_item()
        log.info("getting all the card items")

# Second page - checkout page
        checkout_page: CheckoutPage = CheckoutPage(self.driver)
        products = checkout_page.get_products()

        for product in products:
            product_name = product.find_element_by_xpath("div/h4/a").text
            log.info(product_name)
            if product_name == "iphone X":
                checkout_page.add_product().click()

        checkout_page.checkout()

# Third page - confirmation page
        selected_product = self.driver.find_element_by_xpath("//div[@class='media-body']/h4/a").text

        assert selected_product == "iphone X"

        # self.driver.find_element_by_class_name("btn-success").click()
        final_checkout = ConfirmPage(self.driver)
        final_checkout.get_checkout().click()
        log.info("Entering country name as uni")
        self.driver.find_element_by_id("country").send_keys("uni")
        self.verify_country_name("United States of America")

        countries = final_checkout.select_country()
        for country in countries:
            print(country.text)
            if country.text == "United States of America":
                country.click()
                break

        final_checkout.click_checkbox().click()
        final_checkout.purchase_button()

        alert_success = self.driver.find_element_by_class_name("alert-success").text
        log.info("Text received from the application is" + alert_success)
        assert "Success! Thank you!" in alert_success
        print(alert_success)
        print("Second change")
        print("Third change")
        print("Forth change")
        print("Fifth change")


        print("Last change before merge")
        self.driver.get_screenshot_as_file("e2e_final.jpg")
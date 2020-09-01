import pytest

from selenium import webdriver

from HomePageData import HomePageData
from page_objects import home_page
from page_objects.home_page import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_submission(self, get_data):
        log = self.get_logger()
        homepage = HomePage(self.driver)
        log.info("firstname is " + get_data["firstname"])
        homepage.get_name().send_keys(get_data["firstname"])
        log.info("gender is " + get_data["gender"])
        self.selectOptionByText(homepage.get_gender(), get_data["gender"])
        homepage.submit_form().click()
        alert_text = homepage.get_success_message().text
        assert ("Success" in alert_text)
        self.driver.refresh()

    @pytest.fixture(params = HomePageData.HomePageData.test_HomePage_Data)
    def get_data(self, request):
        return request.param

from selenium.webdriver.common.by import By

# Every page is defined by its own class and includes the objects and methods of this class

class ConfirmPage:

    last_checkout = (By.CLASS_NAME, "btn-success")
    countries_list = (By.XPATH, "//div[@class='suggestions']/ul/li/a")
    check_box = (By.CLASS_NAME, "checkbox-primary")
    purchase = (By.CLASS_NAME, "btn-success")

    def __init__(self, driver: object) -> object:
        self.driver = driver

    def get_checkout(self):                           # class method
        return self.driver.find_element(*ConfirmPage.last_checkout)

    def select_country(self):
        return self.driver.find_elements(*ConfirmPage.countries_list)

    def click_checkbox(self):
        return self.driver.find_element(*ConfirmPage.check_box)

    # This method is the trigger for the transition to the next page (here this is the clicking "purchase button")
    # Here this is the last one page
    def purchase_button(self):
        self.driver.find_element(*ConfirmPage.purchase).click()  # "*" for define tuple type, not list, immutable
        final_checkout = ConfirmPage(self.driver)
        return final_checkout


from selenium.webdriver.common.by import By


# Every page is defined by its own class and includes the objects and methods of this class
class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href='/angularpractice/shop']")  # searching by locator
    name = (By.CSS_SELECTOR, "[name='name']")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    success_message = (By.CSS_SELECTOR, "[class*='alert-success']")

    # This method is the trigger for the transition to the next page (here this is the clicking "shop button")
    def shop_item(self):
        self.driver.find_element(*HomePage.shop).click()  # "*" for define tuple type, not list, immutable
        home_page = HomePage(self.driver)
        return home_page

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def submit_form(self):
        return self.driver.find_element(*HomePage.submit)

    def get_success_message(self):
        return self.driver.find_element(*HomePage.success_message)

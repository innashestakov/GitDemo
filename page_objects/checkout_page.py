from selenium.webdriver.common.by import By

# Every page is defined by its own class and includes the objects and methods of this class

class CheckoutPage:
    # driver.find_elements_by_xpath("//div[@class='card h-100']" - selector of this element
    product = (By.XPATH, "//div[@class='card h-100']")  # class object, products on page
    product_choice = (By.CSS_SELECTOR, ".card-footer button")
    checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def __init__(self, driver):
        self.driver = driver

    def get_products(self):                           # class method
        return self.driver.find_elements(*CheckoutPage.product)

    def add_product(self) -> object:
        return self.driver.find_element(*CheckoutPage.product_choice)

    # This method is the trigger for the transition to the next page (here this is the clicking "checkout button")
    def checkout(self):
        self.driver.find_element(*CheckoutPage.checkout_button).click()  # "*" for define tuple type, not list, immutable
        checkout_page = CheckoutPage(self.driver)
        return checkout_page
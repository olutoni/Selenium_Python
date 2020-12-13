from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    productCards = (By.XPATH, '//div[@class="card h-100"]')
    addButton = (By.XPATH, 'div[2]/button')
    checkoutButton = (By.CLASS_NAME, 'btn-primary')
    finalCheckoutButton = (By.XPATH, '//button[@class="btn btn-success"]')

    def get_products(self):
        return self.driver.find_elements(*CheckoutPage.productCards)

    def get_add_button(self):
        return self.driver.find_element(*CheckoutPage.addButton)

    def get_checkout_button(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton)

    def get_final_checkout_button(self):
        return self.driver.find_element(*CheckoutPage.finalCheckoutButton)


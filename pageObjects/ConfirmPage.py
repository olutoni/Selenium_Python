from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    deliveryLocation = (By.ID, 'country')
    # waitSuggestions = (By.XPATH, "//div[@class='suggestions']/ul/li/a")
    # waitSuggestions = (By.LINK_TEXT, 'United States of America')
    deliveryCountries = (By.XPATH, "//div[@class='suggestions']/ul/li/a")
    selectedCountry = (By.ID, 'country')
    confirmCheckbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitButton = (By.CSS_SELECTOR, '[type="submit"]')
    successMessage = (By.CLASS_NAME, 'alert-success')

    def get_delivery_location(self):
        return self.driver.find_element(*ConfirmPage.deliveryLocation)

    # def get_wait_suggestions(self):
    #     return self.driver.find_element(*ConfirmPage.waitSuggestions)

    def get_delivery_countries(self):
        return self.driver.find_elements(*ConfirmPage.deliveryCountries)

    def get_selected_country(self):
        return self.driver.find_element(*ConfirmPage.selectedCountry)

    def get_checkbox(self):
        return self.driver.find_element(*ConfirmPage.confirmCheckbox)

    def get_submit_button(self):
        return self.driver.find_element(*ConfirmPage.submitButton)

    def get_success_message(self):
        return self.driver.find_element(*ConfirmPage.successMessage)

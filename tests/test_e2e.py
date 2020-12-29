import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures('setup')


class TestOne(BaseClass):

    def test_e2e(self):
        home_page = HomePage(self.driver)
        checkout_page = home_page.shop_button()

        #checkout_page = CheckoutPage(self.driver)
        products = checkout_page.get_products()

        for product in products:
            product_name = product.text
            print(product_name)
            if product_name == 'Blackberry':
                checkout_page.get_add_button().click()

        checkout_page.get_checkout_button().click()
        # confirm_page = ConfirmPage(self.driver)
        confirm_page = checkout_page.get_final_checkout_button()

        confirm_page.get_delivery_location().send_keys('uni')
        self.verify_link_presence('United States of America')

        countries = confirm_page.get_delivery_countries()
        print(len(countries))
        for country in countries:
            if country.text == 'United States of America':
                country_value = country.text
                print(country_value)
                country.click()
                break
        assert confirm_page.get_selected_country().get_attribute(
            'value') == 'United States of America'
        # "//div[@class='suggestions']/ul/li/a"
        confirm_page.get_checkbox().click()
        confirm_page.get_submit_button().click()
        success_message = confirm_page.get_success_message().text
        assert 'Success! Thank you!' in success_message
        self.driver.get_screenshot_as_file("screen.png")

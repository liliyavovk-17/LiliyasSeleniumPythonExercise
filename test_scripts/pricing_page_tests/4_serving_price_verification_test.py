from selenium import webdriver
from pages.base_page import BasePage
from pages.pricing_page import NavigateToPricingPage
from pages.pricing_page import FourServingPricingPageVerifications


# On the Pricing page, verify 4-Serving Signature plan costs $8.99 per serving, FREE shipping, and $71.92 total.

class FourServingModulePricingTest(BasePage):

    def navigate_to_pricing_page(self):
        NavigateToPricingPage(self.driver)

    def assert_two_serving_module_exists(self):
        four_serving_module = FourServingPricingPageVerifications(self.driver)
        four_serving_module.four_serving_three_recipes_module_visible_assertion()

    def assert_cost_per_portion(self):
        cost_per_portion = FourServingPricingPageVerifications(self.driver)
        cost_per_portion.four_serving_three_recipes_module_cost_per_portion_assertion()

    def assert_shipping_price(self):
        shipping_price = FourServingPricingPageVerifications(self.driver)
        shipping_price.four_serving_three_recipes_module_shipping_price_assertion()

    def assert_total_price(self):
        total_price = FourServingPricingPageVerifications(self.driver)
        total_price.four_serving_three_recipes_module_total_price_assertion()

    def tear_down(self):
        self.driver.close()

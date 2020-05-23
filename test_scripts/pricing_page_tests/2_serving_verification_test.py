from selenium import webdriver
from pages.base_page import BasePage
from pages.pricing_page import TwoServingPricingPageVerifications
from pages.pricing_page import NavigateToPricingPage

# On the Pricing page, verify 2-Serving Signature plan costs $9.99 per serving, FREE shipping, and $59.94 total.

class TestTwoServingModulePricing(BasePage)

	def navigate_to_pricing_page(self):
        NavigateToPricingPage(self.driver)

    def assert_two_serving_module_exists(self):
    	two_serving_module = TwoServingPricingPageVerifications(self.driver)
    	two_serving_module.two_serving_three_recipes_module_visible_assertion()

    def assert_cost_per_portion(self):
    	cost_per_portion = TwoServingPricingPageVerifications(self.driver)
    	cost_per_portion.two_serving_three_recipes_module_cost_per_portion_assertion()

    def assert_shipping_price(self):
    	shipping_price = TwoServingPricingPageVerifications(self.driver)
    	shipping_price.two_serving_three_recipes_module_shipping_price_assertion()

    def assert_total_price(self):
    	total_price = TwoServingPricingPageVerifications(self.driver)
    	total_price.two_serving_three_recipes_module_total_price_assertion()

    def tearDown(self):
        self.driver.close()
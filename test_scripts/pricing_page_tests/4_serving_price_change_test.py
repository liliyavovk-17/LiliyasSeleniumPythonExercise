from selenium import webdriver
from pages.base_page import BasePage
from pages.pricing_page import NavigateToPricingPage
from pages.pricing_page import FourServingPricingPageVerifications
from pages.pricing_page import FourServingPricingChangePageVerifications


# On the Pricing page, change 4-Serving Signature from two to three recipes per week.  Verify price has changed to $7.99 per serving and $95.88 total.

class TwoServingPortionChangePricingTest(BasePage):

    def navigate_to_pricing_page(self):
        NavigateToPricingPage(self.driver)

    def assert_four_serving_module_exists(self):
        four_serving_module = FourServingPricingPageVerifications(self.driver)
        four_serving_module.four_serving_three_recipes_module_visible_assertion()

    def change_portions_two(self):
        change_portions_amount = FourServingPricingChangePageVerifications(self.driver)
        change_portions_amount.four_serving_two_recipes_module_change_amount_portions_to_three()

    def assert_cost_per_portion(self):
        cost_per_portion = FourServingPricingChangePageVerifications(self.driver)
        cost_per_portion.four_serving_two_recipes_module_change_amount_portions_to_three()

    def assert_shipping_price(self):
        shipping_price = FourServingPricingChangePageVerifications(self.driver)
        shipping_price.four_serving_two_recipes_module_correct_shipping_price_assertion()

    def assert_total_price(self):
        total_price = FourServingPricingChangePageVerifications(self.driver)
        total_price.four_serving_two_recipes_module_correct_total_price_assertion()

    def tear_down(self):
        self.driver.close()

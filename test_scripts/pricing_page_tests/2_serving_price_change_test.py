from selenium import webdriver
from pages.base_page import BasePage
from pages.pricing_page import NavigateToPricingPage
from pages.pricing_page import TwoServingPricingPageVerifications
from pages.pricing_page import TwoServingPricingChangePageVerifications

# On the Pricing page, change 2-Serving Signature from three recipes to two recipes per week.  Verify prices are $9.99 per serving, $7.99 shipping, and $47.95 total.

class TwoServingPortionChangePricingTest(BasePage)

	def navigate_to_pricing_page(self):
		NavigateToPricingPage(self.driver)

	def assert_two_serving_module_exists(self):
		two_serving_module = TwoServingPricingPageVerifications(self.driver)
		two_serving_module.two_serving_three_recipes_module_visible_assertion()

	def change_portions_two(self):
		change_portions_amount = TwoServingPricingChangePageVerifications(self.driver)
		change_portions_amount.two_serving_module_change_amount_portions_to_three()

	def assert_cost_per_portion(self):
		cost_per_portion = TwoServingPricingChangePageVerifications(self.driver)
		cost_per_portion.two_serving_two_recipes_module_cost_per_portion_assertion()

	def assert_shipping_price(self):
		shipping_price = TwoServingPricingChangePageVerifications(self.driver)
		shipping_price.two_serving_module_correct_shipping_price_assertion()

	def assert_total_price(self):
		total_price = TwoServingPricingChangePageVerifications(self.driver)
		total_price.two_serving_module_correct_total_price_assertion()

	def tear_down(self):
		self.driver.close()

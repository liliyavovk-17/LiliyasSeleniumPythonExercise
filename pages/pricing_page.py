from pages.base_page import BasePage
from locators import PricingPageLocators

# On the Pricing page, verify 2-Serving Signature plan costs $9.99 per serving, FREE shipping, and $59.94 total.

class NavigateToPricingPage(BasePage):
	def navigate_to_pricing_page(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.blueapron.com/pricing")

class TwoServingPricingPageVerifications(BasePage):
	
	def two_serving_three_recipes_module_visible_assertion(self):
		two_serving_module = self.driver.find_element(*PricingPageLocators.SERVING_2_SERVINGS_NUMBER)
		assert two_serving_module.is_displayed()

	def two_serving_three_recipes_module_cost_per_portion_assertion(self):
		two_serving_module_price = self.driver.find_element(*SERVING_2_COST_PER_SERVING)
		assert two_serving_module_price = '9.99'

	def two_serving_three_recipes_module_shipping_price_assertion(self):
		two_serving_module_price = self.driver.find_element(*SERVING_2_SHIPPING_PRICE)
		assert two_serving_module_price = 'FREE'

	def two_serving_three_recipes_module_total_price_assertion(self):
		two_serving_module_price = self.driver.find_element(*SERVING_2_TOTTAL_PRICE)
		assert two_serving_module_price = '59.94'

# On the Pricing page, verify 4-Serving Signature plan costs $8.99 per serving, FREE shipping, and $71.92 total.
class FourServingPricingPageVerifications(BasePage):

	def four_serving_three_recipes_module_visible_assertion(self):
		four_serving_module_price = self.driver.find_element(*PricingPageLocators.SERVING_2_SERVINGS_NUMBER)
		assert four_serving_module_price.is_displayed()

	def four_serving_three_recipes_module_cost_per_portion_assertion(self):
		four_serving_module_price = self.driver.find_element(*SERVING_2_COST_PER_SERVING)
		assert four_serving_module_price = '8.99'

	def four_serving_three_recipes_module_shipping_price_assertion(self):
		four_serving_module_price = self.driver.find_element(*SERVING_2_SHIPPING_PRICE)
		assert four_serving_module_price = 'FREE'

	def four_serving_three_recipes_module_total_price_assertion(self):
		four_serving_module_price = self.driver.find_element(*SERVING_2_TOTAL_PRICE)
		assert four_serving_module_price = '71.92'

# On the Pricing page, change 2-Serving Signature from three recipes to two recipes per week.  Verify prices are $9.99 per serving, $7.99 shipping, and $47.95 total. 

class TwoServingPricingChangePageVerifications(BasePage):

	def two_serving_module_change_amount_portions_to_three(self):
		change_recipes_per_week = self.driver.find_element(*SERVING_2_RECIPES_PER_WEEK_CHANGE)
		change_recipes_per_week.click()

	def two_serving_two_recipes_module_cost_per_portion_assertion(self):
		two_serving_module_price = self.driver.find_element(*SERVING_2_COST_PER_SERVING)
		assert two_serving_module_price = '9.99'

	def two_serving_module_correct_shipping_price_assertion(self):
		two_serving_module_price = self.driver.find_element(*SERVING_2_SHIPPING_PRICE)
		assert two_serving_module_price = '7.99'

	def two_serving_module_correct_total_price_assertion(self):
		two_serving_module_price = self.driver.find_element(*SERVING_2_TOTAL_PRICE)
		assert two_serving_module_price = '47.95'

# On the Pricing page, change 4-Serving Signature from two to three recipes per week.  Verify price has changed to $7.99 per serving and $95.88 total.

class FourServingPricingChangePageVerifications(BasePage):

	def four_serving_two_recipes_module_change_amount_portions_to_three(self):
		change_recipes_per_week = self.driver.find_element(*SERVING_4_PER_WEEK_CHANGE)
		change_recipes_per_week.click()

	def four_serving_two_recipes_module_change_amount_portions_to_three(self):
		two_recipes_per_week = self.driver.find_element(*SERVING_4_RECIPES_PER_WEEK)
		two_recipes_per_week.click()

	def four_serving_two_recipes_module_cost_per_portion_assertion(self):
		two_serving_module_price = self.driver.find_element(*SERVING_4_COST_PER_SERVING)
		assert two_serving_module_price = '9.99'

	def four_serving_two_recipes_module_correct_shipping_price_assertion(self):
		two_serving_module_price = self.driver.find_element(*SERVING_4_SHIPPING_PRICE)
		assert two_serving_module_price = '7.99'

	def four_serving_two_recipes_module_correct_total_price_assertion(self):
		two_serving_module_price = self.driver.find_element(*SERVING_4_TOTTAL_PRICE)
		assert two_serving_module_price = '47.95'


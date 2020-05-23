from selenium import webdriver
from pages.base_page import BasePage
from pages.pricing_page import NavigateToPricingPage
from pages.pricing_page import TwoServingPricingPageVerifications
from pages.sign_up_page import LandOnSignUpPage
# from pages.sign_up_page import SignUpPage

# From the Pricing page, click any of the Select buttons.  Verify that the user is directed to the Signup page.  


class LandingOnSignUpPage(BasePage):

	def navigate_to_pricing_page(self):
		NavigateToPricingPage(self.driver)

	def assert_two_serving_module_exists(self):
		two_serving_module = TwoServingPricingPageVerifications(self.driver)
		two_serving_module.two_serving_three_recipes_module_visible_assertion()

	def click_select_button(self):
		select_button = LandOnSignUpPage(self.driver)
		select_button.click()
		select_button.assert_landed_on_correct_page()

	def tear_down(self):
		self.driver.close()

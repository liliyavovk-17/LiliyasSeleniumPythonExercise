from selenium import webdriver
from pages.base_page import BasePage
# from pages.pricing_page import NavigateToPricingPage
# from pages.pricing_page import TwoServingPricingPageVerifications
# from pages.sign_up_page import LandOnSignUpPage
from pages.sign_up_page import SignUpPage


# On the Signup page, verify the Apple Sign Up button is displayed.
# On the Signup page, click Continue button without entering email address.  Verify error prompt.

class ContinueWithInvalidEmailSignUpPage(BasePage):

	def navigate_to_sign_up_page(self):
		SignUpPage.navigate_to_sign_up_page(self.driver)

	def click_continue_button(self):
		continue_button = SignUpPage(self.driver)
		continue_button.click_continue_with_invalid_email()

	def verify_error_message(self):
		error_message = SignUpPage(self.driver)
		error_message.verify_error_message()

	def tear_down(self):
		self.driver.close()

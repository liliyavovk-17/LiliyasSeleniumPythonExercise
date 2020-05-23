from selenium import webdriver
from pages.base_page import BasePage
# from pages.pricing_page import NavigateToPricingPage
# from pages.pricing_page import TwoServingPricingPageVerifications
# from pages.sign_up_page import LandOnSignUpPage
from pages.sign_up_page import SignUpPage


# On the Signup page, verify the Apple Sign Up button is displayed.

class AssertAppleIdButtonSignUpPage(BasePage):

    def navigate_to_sign_up_page(self):
        SignUpPage.navigate_to_sign_up_page(self.driver)

    def assert_apple_id_button(self):
        apple_id_button = SignUpPage(self.driver)
        apple_id_button.assert_apple_id_button_visible()

    def tear_down(self):
        self.driver.close()

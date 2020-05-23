from pages.base_page import BasePage
from locators import SignUpPageLocators


# From the Pricing page, click any of the Select buttons.  Verify that the user is directed to the Signup page.  

class LandOnSignUpPage(BasePage):

	def click_select_button(self):
        self.driver.find_element(*SignUpPageLocators.CONTINUE_BUTTON).click()

    def assert_landed_on_correct_page(self):
        driver = self.driver
        driver.getCurrentUrl();
        assert.assertEquals(URL, "https://www.blueapron.com/users/sign_up")


# On the Signup page, verify the Apple Sign Up button is displayed.
# On the Signup page, click Continue button without entering email address.  Verify error prompt.


class SignUpPage(BasePage):

    def navigate_to_sign_up_page(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.blueapron.com/users/sign_up")  

    def assert_apple_id_button_visible(self):
        apple_id_button = self.driver.find_element(*SignUpPageLocators.APPLE_SIGN_UP_BUTTON)
        assert two_serving_module.is_displayed()

    def click_continue_with_invalid_email(self):
        continue_button = self.driver.find_element(*SignUpPageLocators.CONTINUE_BUTTON)
        continue_button.click()

    def verify_error_message(self):
        invalid_email_text = self.driver.find_element(*SignUpPageLocators.INVALID_EMAIL_ERROR_MESSAGE)
        assert invalid_email_text.is_displayed()
    
    def tearDown(self):
        self.driver.close()

from pages.base_page import BasePage
from locators import HomePageLocators


class NavBarHomePage(BasePage):
    traits = [
        HomePageLocators.PRICING_IN_HEADER 
    ]

    # pricing_in_header = NavBarHomePage()
    def navigate_to_home_page(self):
        self.driver = driver
        self.driver.get("http://www.blueapron.com")

    def click_pricing_in_header(self):
        self.driver.find_element(*HomePageLocators.PRICING_IN_HEADER).click()

    def assert_landed_on_correct_page(self):
        String_URL = driver.getCurrentUrl();
        Assert.assertEquals(URL, "https://www.blueapron.com/pricing")

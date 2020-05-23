from selenium import webdriver
from pages.home_page import NavBarHomePage
from pages.base_page import BasePage


class TestNavBarPricingLink(BasePage):

    def navigate_to_home_page(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.blueapron.com")

    def test_pricing_link(self):
        home_page = NavBarHomePage(self.driver)
        home_page.await_traits()
        home_page.click_pricing_in_header()
        home_page.assert_landed_on_correct_page()

    def tearDown(self):
    self.driver.close()

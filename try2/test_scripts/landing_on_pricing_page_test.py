from selenium import webdriver
from try2.pages.home_page import NavBarHomePage

class TestLogin:

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.blueapron.com")

    # def test_one(self):
    #     home_page = NavBarHomePage(self.driver)
    #     NavBarHomePage.click_pricing_in_header()

    def tearDown(self):
        self.driver.close()
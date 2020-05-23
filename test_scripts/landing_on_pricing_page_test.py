from selenium import webdriver
from pages.home_page import NavBarHomePage


class TestNavBarPricingLink():

        
    def test_pricing_link(self, driver):
    	home_page = NavBarHomePage(driver).await_traits()
    	
    	home_page.click_pricing_in_header()
    	home_page.assert_landed_on_correct_page()

    # def tearDown(self):
   	# 	self.driver.close()


   		# onboarding_page = OnboardingPage(driver).await_traits()
     #    onboarding_page.dismiss_onboarding()

     #    location_switcher_page = LocationSwitcherPage(driver).await_traits()
     #    location_switcher_page.choose_location()

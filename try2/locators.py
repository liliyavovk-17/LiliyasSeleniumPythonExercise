from selenium.webdriver.common.by import By


# class HomePageLocators(object):
#     """A class for login page locators."""
# 	# PRICING_IN_HEADER = driver.find_elements(By.XPATH, "//a[@class='nav_pricing']")
# 	NAV_BAR_PRICING_BUTTON = driver.find_elements(By.XPATH, "//a[@class=nav_pricing]")


class HomePageLocators(object):
	"""A class for checkout page locators."""
	# PRICING_IN_HEADER = (By.XPATH, "//a[@class='nav_pricing']")
	PRICING_IN_HEADER = (By.XPATH, "//a[@class='nav_pricing']")
   	APPLE_SIGN_UP_BUTTON = (By.ID, "appleid-signin")
	CONTINUE_BUTTON = (By.XPATH, "//button[@class=pom-Button pom-Button--blue pom-Button--filled pom-Button--full]")
	# "//div[@class='pom-Button--mouseover'][contains(text(),'Continue')]")
	# INVALID_EMAIL_ERROR = (By.XPATH, "//div[@class='pom-InputError']")
	# [contains(text(),'Pricing')]

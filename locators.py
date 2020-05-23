from selenium.webdriver.common.by import By


class HomePageLocators(object):
    """A class for login page locators."""
    PRICING_IN_HEADER = (By.XPATH, "//a[@class='nav_pricing'][contains(text(),'Pricing')]")


class PricingPageLocators(object):
    """A class for pricing page locators."""
    
    SERVING_2_SERVINGS_NUMBER = (By.XPATH, "//h1[@class='pom-PlanCard__name'][contains(text(),'Signature')]")
    SERVING_2_COST_PER_SERVING = (By.XPATH, "//div[@class='pom-PlanCard__price pom-PlanCard__price-serving'][0]")
    SERVING_2_SHIPPING_PRICE = (By.XPATH, "//strong[@class='pom-PlanCard-price__amount][0]")
    SERVING_2_RECIPES_PER_WEEK_CHANGE = (By.CSS_SELECTOR, "pom-QuantitySelector.pom-QuantitySelector__rectangle[0] li:nth-of-type(1)")
    SERVING_2_TOTAL_PRICE = (By.XPATH, "//div[@class='pom-PlanCard__price.pom-PlanCard__price--total'][0]")

    SERVING_4_SERVINGS_NUMBER = (By.XPATH, "//h1[@class='pom-PlanCard__name'][contains(text(),'Signature for 4')]")
    SERVING_4_COST_PER_SERVING = (By.XPATH, "//div[@class='pom-PlanCard__price pom-PlanCard__price-serving'][1]")
    SERVING_4_SHIPPING_PRICE = (By.XPATH, "//strong[@class='pom-PlanCard-price__amount][3]")
    SERVING_4_PER_WEEK_CHANGE = (By.CSS_SELECTOR, "pom-QuantitySelector.pom-QuantitySelector__rectangle[0] li:nth-of-type(1)")
    SERVING_4_TOTAL_PRICE = (By.XPATH, "//div[@class='pom-PlanCard__price.pom-PlanCard__price--total'][1]")

    SELECT_BUTTON = (By.CLASS_NAME, "om-Button pom-Button--blue pom-Button--pill-filled pom-Button--full")
    # "//div[@class='pom-Button--mouseover'][contains(text(),'Select')]")


class SignUpPageLocators(object):
    """A class for checkout page locators."""
    APPLE_SIGN_UP_BUTTON = (By.ID, "appleid-signin")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "pom-Button.pom-Button--blue.pom-Button--filled.pom-Button--full")
    # "//div[@class='pom-Button--mouseover'][contains(text(),'Continue')]")
    INVALID_EMAIL_ERROR_MESSAGE = (By.XPATH, "//div[@class='pom-InputError']")






    # PASSWORD_INPUT = (By.NAME, "password")
    # LOG_IN_BUTTON = (By.CSS_SELECTOR, "button.login-button")
    # FORGOT_PASSWORD_BUTTON = (By.CLASS_NAME, "forgot-password")
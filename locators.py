from selenium.webdriver.common.by import By


SIGN_IN_MENU = (By.CSS_SELECTOR, ".ow_signin_label")

USERNAME_FIELD = (By.NAME, "identity")
PASSWORD_FIELD = (By.NAME, "password")
SIGN_IN_BUTTON = (By.NAME, 'submit')

POST_BLOCK = (By.CLASS_NAME, "ow_newsfeed_item")

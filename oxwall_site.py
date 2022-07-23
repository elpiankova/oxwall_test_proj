from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from custom_wait_conditions import presents_of_number_of_elements_located


class OwxallSite:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        sign_in_menu = self.driver.find_element(By.CSS_SELECTOR, ".ow_signin_label")
        sign_in_menu.click()
        username_field = self.driver.find_element(By.NAME, "identity")
        username_field.clear()
        username_field.send_keys("admin")
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.clear()
        password_field.send_keys("pass")
        sign_in_button = self.driver.find_element(By.NAME, 'submit')
        sign_in_button.click()

    def logout(self):
        # TODO: logout
        pass

    def get_text_of_first_post(self, posts):
        # Get text of new post
        post_text = posts[0].find_element(By.CLASS_NAME, "ow_newsfeed_content").text
        return post_text

    def wait_new_post_appear(self, initial_amount_of_posts):
        # Wait new post
        wait = WebDriverWait(self.driver, 5)
        posts = wait.until(
            presents_of_number_of_elements_located((By.CLASS_NAME, "ow_newsfeed_item"), initial_amount_of_posts + 1),
            message="Can't find visible Post text field"
        )
        return posts

    def submit_post(self):
        # Submit post
        save_button = self.driver.find_element(By.NAME, 'save')
        save_button.click()

    def input_text_of_new_post(self, input_text):
        wait = WebDriverWait(self.driver, 5)
        post_field = wait.until(EC.visibility_of_element_located((By.NAME, 'status')),
                                message="Can't find visible Post text field")
        # post_field = driver.find_element(By.NAME, 'status')
        post_field.click()
        post_field.send_keys(input_text)
        return wait

    def calculate_posts(self):
        # Calculate existed posts
        posts = self.driver.find_elements(By.CLASS_NAME, "ow_newsfeed_item")
        initial_amount_of_posts = len(posts)
        return initial_amount_of_posts

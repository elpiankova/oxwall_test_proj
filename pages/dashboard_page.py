from selenium.webdriver.common.by import By

from custom_wait_conditions import presents_of_number_of_elements_located
from pages.internal_page import InternalPage
from pages.locators import DashboardPageLocators
from pages.elements.post_block import PostBlock


class DashboardPage(InternalPage):
    @property
    def title(self):
        return self.find_visible_element(DashboardPageLocators.TITLE)

    @property
    def posts(self):
        return self.find_elements(DashboardPageLocators.POST_BLOCK)

    @property
    def post_text_field(self):
        return self.find_visible_element(DashboardPageLocators.STATUS_FIELD)

    @property
    def send_bt(self):
        return self.find_element(DashboardPageLocators.SAVE_BT)

    def is_this_page(self):
        if self.title.text == "MY DASHBOARD" and self.active_menu.text == "DASHBOARD":
            return True
        else:
            return False

    def wait_new_post_appear(self, initial_amount_of_posts):
        # Wait new post
        posts = self.wait.until(
            presents_of_number_of_elements_located(DashboardPageLocators.POST_BLOCK, initial_amount_of_posts + 1),
            message="Can't find visible Post text field"
        )
        return posts

    def submit_post(self):
        # Submit post
        save_button = self.driver.find_element(By.NAME, 'save')
        save_button.click()

    def input_text_of_new_post(self, input_text):
        self.post_text_field.click()
        self.post_text_field.clear()
        self.post_text_field.send_keys(input_text)

    def calculate_posts(self):
        initial_amount_of_posts = len(self.posts)
        return initial_amount_of_posts

    def get_text_of_first_post(self, posts):
        # Get text of new post
        post_text = posts[0].find_element(By.CLASS_NAME, "ow_newsfeed_content").text
        return post_text

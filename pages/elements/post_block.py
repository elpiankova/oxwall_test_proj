from pages.locators import PostBlockLocators


class PostBlock:
    def __init__(self, element):
        self.element = element

    @property
    def user(self):
        return self.element.find_element(*PostBlockLocators.POST_USER).text

    @property
    def text(self):
        return self.element.find_element(*PostBlockLocators.POST_TEXT).text

    @property
    def time(self):
        return self.element.find_element(*PostBlockLocators.POST_TIME).text

    @property
    def like_bt(self):
        return self.element.find_element(*PostBlockLocators.LIKE)

    def add_like(self):
        self.like_bt.click()

import json

import pytest

from pages.dashboard_page import DashboardPage
from data.random_string import random_string

with open("data/posts_text.json", encoding="utf8") as f:
    posts_text = json.load(f)

posts_text.append(random_string(minlen=3, maxlen=30, enter=True, cyrillic=True))


@pytest.mark.parametrize("input_text", posts_text)
def test_create_post(driver, open_oxwall_site, logged_user, input_text):
    dashboard_page = DashboardPage(driver)
    initial_amount_of_posts = dashboard_page.calculate_posts()
    dashboard_page.input_text_of_new_post(input_text)
    dashboard_page.submit_post()
    dashboard_page.wait_new_post_appear(initial_amount_of_posts)
    posts = dashboard_page.posts
    new_post = posts[0]
    new_post.add_like()
    # post_text = dashboard_page.get_text_of_first_post(posts)
    assert new_post.text == input_text
    assert new_post.user == logged_user.username.title()


def test_add_like_to_middle_post(driver, open_oxwall_site, logged_user):
    dashboard_page = DashboardPage(driver)
    posts = dashboard_page.posts
    middle_post = posts[len(posts)//2]
    middle_post.add_like()
    assert middle_post.like_counter.text == "1"


def test_submit_post_without_text(driver, open_oxwall_site, login):
    dashboard_page = DashboardPage(driver)
    initial_amount_of_posts = dashboard_page.calculate_posts()
    dashboard_page.submit_post()
    posts = dashboard_page.calculate_posts()
    assert initial_amount_of_posts == posts

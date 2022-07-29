from pages.dashboard_page import DashboardPage
from pages.elements.post_block import PostBlock


def test_create_post(driver, open_oxwall_site, logged_user):
    input_text = "Miklail is telling you about his status"
    dashboard_page = DashboardPage(driver)

    initial_amount_of_posts = dashboard_page.calculate_posts()
    dashboard_page.input_text_of_new_post(input_text)
    dashboard_page.submit_post()
    posts = dashboard_page.wait_new_post_appear(initial_amount_of_posts)
    new_post = PostBlock(posts[0])
    # post_text = dashboard_page.get_text_of_first_post(posts)
    assert new_post.text == input_text
    assert new_post.user == logged_user.title()


def test_submit_post_without_text(driver, open_oxwall_site, login):
    dashboard_page = DashboardPage(driver)
    initial_amount_of_posts = dashboard_page.calculate_posts()
    dashboard_page.submit_post()
    posts = dashboard_page.calculate_posts()
    assert initial_amount_of_posts == posts

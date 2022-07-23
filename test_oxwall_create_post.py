from oxwall_site import OwxallSite


def test_create_post(driver, open_oxwall_site, login):
    input_text = "Miklail is telling you about his status"
    app = OwxallSite(driver)

    initial_amount_of_posts = app.calculate_posts()
    app.input_text_of_new_post(input_text)
    app.submit_post()
    posts = app.wait_new_post_appear(initial_amount_of_posts)
    post_text = app.get_text_of_first_post(posts)
    assert post_text == input_text

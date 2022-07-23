from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from custom_wait_conditions import presents_of_number_of_elements_located


def test_create_post():
    input_text = "Miklail is telling you about his status"

    driver = webdriver.Chrome()
    driver.implicitly_wait(15)

    # Login
    sign_in_menu = driver.find_element(By.CSS_SELECTOR, ".ow_signin_label")
    sign_in_menu.click()
    username_field = driver.find_element(By.NAME, "identity")
    username_field.clear()
    username_field.send_keys("admin")
    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys("pass")
    sign_in_button = driver.find_element(By.NAME, 'submit')
    sign_in_button.click()

    # Calculate existed posts
    posts = driver.find_elements(By.CLASS_NAME, "ow_newsfeed_item")
    initial_amount_of_posts = len(posts)

    # Input text of new post
    wait = WebDriverWait(driver, 5)
    post_field = wait.until(EC.visibility_of_element_located((By.NAME, 'status')),
                            message="Can't find visible Post text field")
    # post_field = driver.find_element(By.NAME, 'status')
    post_field.click()

    # Submit post
    save_button = driver.find_element(By.NAME, 'save')
    save_button.click()

    # Wait new post
    wait = WebDriverWait(driver, 5)
    posts = wait.until(
        presents_of_number_of_elements_located((By.CLASS_NAME, "ow_newsfeed_item"), initial_amount_of_posts + 1),
        message="Can't find visible Post text field"
    )

    # Get text of new post
    post_text = posts[0].find_element(By.CLASS_NAME, "ow_newsfeed_content").text
    assert post_text == input_text

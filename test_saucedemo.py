
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Test 1: Verify successful login
def test_saucedemo_login():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 15)

        # Enter login credentials
        wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")

        driver.find_element(
            By.ID, "password"
        ).send_keys("secret_sauce")

        driver.find_element(
            By.ID, "login-button"
        ).click()

        # Verify successful login
        wait.until(EC.url_contains("inventory.html"))
        assert "inventory.html" in driver.current_url

        print("Login test passed successfully!")

    finally:
        driver.quit()


# Test 2: Verify shopping cart functionality
def test_add_products_to_cart():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 15)

        # Log in
        wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")

        driver.find_element(
            By.ID, "password"
        ).send_keys("secret_sauce")

        driver.find_element(
            By.ID, "login-button"
        ).click()

        wait.until(EC.url_contains("inventory.html"))

        # Add two products
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        ).click()

        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-bike-light")
            )
        ).click()

        # Verify cart badge
        cart_badge = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "shopping_cart_badge")
            )
        )

        assert cart_badge.text == "2"
        print("Shopping cart badge correctly displays 2 items!")

        # Open shopping cart
        wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        ).click()

        wait.until(EC.url_contains("cart.html"))

        # Verify both products
        product_names = [
            item.text for item in driver.find_elements(
                By.CLASS_NAME, "inventory_item_name"
            )
        ]

        assert "Sauce Labs Backpack" in product_names
        assert "Sauce Labs Bike Light" in product_names

        print("Both products verified in the shopping cart!")

    finally:
        driver.quit()


# Test 3: Verify complete checkout process
def test_complete_checkout():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 15)

        # Log in
        wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")

        driver.find_element(
            By.ID, "password"
        ).send_keys("secret_sauce")

        driver.find_element(
            By.ID, "login-button"
        ).click()

        wait.until(EC.url_contains("inventory.html"))

        # Add two products to the cart
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        ).click()

        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-bike-light")
            )
        ).click()

        # Open shopping cart
        wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        ).click()

        wait.until(EC.url_contains("cart.html"))

        # Click Checkout
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "checkout")
            )
        ).click()

        wait.until(EC.url_contains("checkout-step-one.html"))

        # Enter fictional customer information
        driver.find_element(
            By.ID, "first-name"
        ).send_keys("John")

        driver.find_element(
            By.ID, "last-name"
        ).send_keys("Smith")

        driver.find_element(
            By.ID, "postal-code"
        ).send_keys("00100")

        # Continue to checkout overview
        driver.find_element(
            By.ID, "continue"
        ).click()

        wait.until(EC.url_contains("checkout-step-two.html"))

        # Verify checkout total
        total = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )

        assert total.text == "Total: $43.18"
        print("Checkout total verified: $43.18")

        # Complete the order
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "finish")
            )
        ).click()

        wait.until(EC.url_contains("checkout-complete.html"))

        # Verify confirmation message
        confirmation = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "complete-header")
            )
        )

        assert confirmation.text == "Thank you for your order!"

        print("Checkout completed successfully!")
        print("Order confirmation verified!")

    finally:
        driver.quit()

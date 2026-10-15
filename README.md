# SauceDemo UI Testing with Selenium

## Project Overview

This project demonstrates automated user interface testing of the [SauceDemo](https://www.saucedemo.com/) e-commerce website using Python, Selenium WebDriver, and Pytest.

The project was developed as part of a UI testing assignment at LAB University of Applied Sciences.

## Technologies Used

- Python 3.10
- Selenium WebDriver
- Pytest
- Google Chrome
- Visual Studio Code
- Chrome DevTools (for manual performance testing)

## Automated Test Cases

**Test 1 — Login Verification**

Logs in using the standard SauceDemo test credentials and verifies successful navigation to the inventory page.

**Test 2 — Shopping Cart Verification**

Adds the Sauce Labs Backpack and Sauce Labs Bike Light to the shopping cart, verifies the cart badge displays two items, and checks that both products appear in the cart.

**Test 3 — Complete Checkout Process**

Logs in, adds two products to the cart, enters fictional customer information, verifies the order total of $43.18, completes checkout, and checks the order confirmation message.

## Installation

1. Clone the repository:

   `git clone https://github.com/YOUR_USERNAME/saucedemo-selenium-ui-testing.git`

2. Open the project folder.

3. Create a Python virtual environment:

   `python -m venv .venv`

4. Activate the virtual environment on Windows:

   `.venv\Scripts\activate`

5. Install the required packages:

   `pip install -r requirements.txt`

## Running the Tests

Execute the following command:

`python -m pytest -s test_saucedemo.py`

## Test Results

All three automated tests passed successfully during development.

## Manual Performance Testing

Chrome DevTools was also used to investigate mobile responsiveness, network performance, CPU throttling, loading times, and the checkout experience.

## Author

Nicolae Dobinda

LAB University of Applied Sciences

Information Technology
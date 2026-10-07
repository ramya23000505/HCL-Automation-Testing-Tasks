from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


# ============================================================
# 1. START BROWSER
# ============================================================

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 30)

print("STEP 1: Browser started")


# ============================================================
# 2. OPEN AMAZON
# ============================================================

driver.get("https://www.amazon.in/")

print("STEP 2: Amazon opened")


# ============================================================
# 3. OPEN ACCOUNT / LOGIN
# ============================================================

try:

    account = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "nav-link-accountList")
        )
    )

    account.click()

    print("STEP 3: Login page opened")

except Exception as e:

    print("Could not open Amazon login.")
    print("Error:", e)

    input("Press ENTER to close...")
    driver.quit()
    exit()


# ============================================================
# 4. MANUAL LOGIN
# ============================================================

print()
print("==============================================")
print("MANUAL LOGIN REQUIRED")
print("==============================================")
print()
print("Complete the following in the browser:")
print("1. Enter your Amazon email/mobile")
print("2. Enter your password")
print("3. Enter OTP if requested")
print("4. Complete CAPTCHA/security verification if shown")
print("5. Wait until Amazon home page is visible")
print()
print("DO NOT enter your password into this Python file.")
print()


input(
    "After you are completely logged in, "
    "press ENTER here..."
)


# ============================================================
# 5. VERIFY AMAZON HOME PAGE
# ============================================================

print()
print("STEP 4: Checking Amazon login...")


try:

    search_box = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "twotabsearchtextbox")
        )
    )

    print("STEP 5: Amazon homepage confirmed")
    print("STEP 6: Search box found")


except TimeoutException:

    print()
    print("ERROR: Amazon search box was not found.")
    print()
    print("Current URL:", driver.current_url)
    print("Page title:", driver.title)
    print()
    print("Make sure login is completely finished.")

    input("Press ENTER to close...")

    driver.quit()
    exit()


# ============================================================
# 6. SEARCH PRODUCT
# ============================================================

print()
print("STEP 7: Searching product...")


search_box.click()
search_box.clear()

search_box.send_keys("wireless mouse")

print("STEP 8: Product name entered")

search_box.send_keys(Keys.ENTER)

print("STEP 9: Search submitted")


# ============================================================
# 7. WAIT FOR SEARCH RESULTS
# ============================================================

try:

    products = wait.until(
        EC.presence_of_all_elements_located(
            (
                By.CSS_SELECTOR,
                "div[data-component-type='s-search-result'][data-asin]"
            )
        )
    )

    print("STEP 10: Search results loaded")
    print("Products found:", len(products))


except TimeoutException:

    print()
    print("ERROR: Search results were not found.")
    print("Current URL:", driver.current_url)
    print("Page title:", driver.title)

    input("Press ENTER to close...")

    driver.quit()
    exit()


# ============================================================
# 8. FIND FIRST PRODUCT ASIN
# ============================================================

selected_asin = None

for product in products:

    asin = product.get_attribute("data-asin")

    if asin:

        selected_asin = asin

        print(
            "STEP 11: Product selected"
        )

        print(
            "ASIN:",
            selected_asin
        )

        break


if selected_asin is None:

    print("ERROR: No product ASIN found.")

    input("Press ENTER to close...")

    driver.quit()
    exit()


# ============================================================
# 9. OPEN PRODUCT PAGE
# ============================================================

product_url = (
    f"https://www.amazon.in/dp/{selected_asin}"
)

print()
print("STEP 12: Opening product page...")
print(product_url)

driver.get(product_url)


# ============================================================
# 10. VERIFY PRODUCT PAGE
# ============================================================

try:

    product_title = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "productTitle")
        )
    )

    print("STEP 13: Product page loaded")

    print(
        "Product:",
        product_title.text.strip()
    )


except TimeoutException:

    print("ERROR: Product page did not load.")
    print("Current URL:", driver.current_url)

    input("Press ENTER to close...")

    driver.quit()
    exit()


# ============================================================
# 11. ADD TO CART
# ============================================================

print()
print("STEP 14: Looking for Add to Cart...")


try:

    add_to_cart = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-button")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        add_to_cart
    )

    time.sleep(1)

    add_to_cart.click()

    print("STEP 15: Product added to cart")


except Exception as e:

    print("ERROR: Could not add product to cart.")
    print("Error:", e)

    input("Press ENTER to close...")

    driver.quit()
    exit()


# ============================================================
# 12. OPEN CART
# ============================================================

time.sleep(3)

print()
print("STEP 16: Opening cart...")


try:

    cart = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "nav-cart")
        )
    )

    cart.click()

    print("STEP 17: Cart opened")


except Exception as e:

    print("Cart click failed.")
    print("Opening cart directly...")

    driver.get(
        "https://www.amazon.in/gp/cart/view.html"
    )

    print("STEP 17: Cart opened directly")


# ============================================================
# 13. WAIT FOR CART
# ============================================================

time.sleep(3)

print("Cart URL:", driver.current_url)


# ============================================================
# 14. PROCEED TO BUY
# ============================================================

print()
print("STEP 18: Looking for Proceed to Buy...")


try:

    proceed = wait.until(
        EC.element_to_be_clickable(
            (
                By.NAME,
                "proceedToRetailCheckout"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        proceed
    )

    time.sleep(1)

    proceed.click()

    print("STEP 19: Proceed to Buy clicked")


except Exception as e:

    print("ERROR: Could not click Proceed to Buy.")
    print("Error:", e)

    input("Press ENTER to close...")

    driver.quit()
    exit()


# ============================================================
# 15. WAIT FOR CHECKOUT
# ============================================================

print()
print("STEP 20: Waiting for checkout page...")

time.sleep(5)


print()
print("==============================================")
print("CHECKOUT PAGE REACHED")
print("==============================================")

print("Current URL:")
print(driver.current_url)

print()
print("Page title:")
print(driver.title)


# ============================================================
# 16. STOP BEFORE PAYMENT
# ============================================================

print()
print("==============================================")
print("AUTOMATION COMPLETED")
print("==============================================")

print("Amazon opened       : DONE")
print("Login               : MANUAL")
print("OTP                 : MANUAL")
print("Product search      : DONE")
print("Product selection   : DONE")
print("Add to cart         : DONE")
print("Cart                : DONE")
print("Proceed to Buy      : DONE")
print("Payment             : NOT PERFORMED")
print("Order               : NOT PLACED")

print("==============================================")


input(
    "\nPress ENTER to close the browser..."
)


# ============================================================
# 17. CLOSE
# ============================================================

driver.quit()

print("Browser closed.")
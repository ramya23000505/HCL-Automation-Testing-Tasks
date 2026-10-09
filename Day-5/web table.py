'''Ramya R(212223230169)'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
'''1. Read the table data'''
try:
    driver.get("https://the-internet.herokuapp.com/tables")
    driver.maximize_window()
    table = driver.find_element(By.ID, "table1")
    rows = table.find_elements(By.TAG_NAME, "tr")
    print("Total rows including header:", len(rows))
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "th")

        if not cells:
            cells = row.find_elements(By.TAG_NAME, "td")

        row_data = [cell.text for cell in cells]
        print(row_data)

finally:
    time.sleep(10)
    driver.quit()


'''2. Get specific row and column data'''


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
try:
    driver.get("https://the-internet.herokuapp.com/tables")

    table = driver.find_element(By.ID, "table1")

    # Get all data rows, excluding the header
    rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")

    # First data row
    first_row = rows[0]

    # Get all cells in the row
    cells = first_row.find_elements(By.TAG_NAME, "td")

    # First column: Last Name
    print("Last Name:", cells[0].text)

    # Second column: First Name
    print("First Name:", cells[1].text)

    # Third column: Email
    print("Email:", cells[2].text)

finally:
    time.sleep(10)
    driver.quit()

'''3. Searching Program'''


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
try:
    driver.get("https://the-internet.herokuapp.com/tables")

    rows = driver.find_elements(
        By.CSS_SELECTOR, "#table1 tbody tr"
    )

    search_name = "John"
    found = False

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")

        first_name = cells[1].text

        if first_name == search_name:
            print("Employee found!")
            print("Employee details:", row.text)
            found = True
            break

    if not found:
        print("Employee not found")

finally:
    time.sleep(10)
    driver.quit()

'''
4. count the rows and columns
'''


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
try:
    driver.get("https://the-internet.herokuapp.com/tables")

    table = driver.find_element(By.ID, "table1")

    rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")
    headers = table.find_elements(By.CSS_SELECTOR, "thead th")

    print("Number of data rows:", len(rows))
    print("Number of columns:", len(headers))

finally:
    time.sleep(10)
    driver.quit()
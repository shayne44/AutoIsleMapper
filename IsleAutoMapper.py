from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pyperclip

# Web driver init + load
driver = webdriver.Chrome()
driver.get("https://vulnona.com/game/the_isle/#")

# Wait for load and ID input + submit
wait = WebDriverWait(driver, 10)
input_field = wait.until(EC.presence_of_element_located((By.ID, "my_loc")))
submit_button = wait.until(EC.presence_of_element_located((By.ID, "my_loc_submit")))

# Get clipboard text
clipboard_content = pyperclip.paste()

while True:
    # check clipboard 0.5 second intervals
    time.sleep(0.5)
    new_clipboard_content = pyperclip.paste()
    if new_clipboard_content != clipboard_content:
        clipboard_content = new_clipboard_content
        # paste the clipboard
        input_field.clear()
        input_field.send_keys(clipboard_content)
        submit_button.click()

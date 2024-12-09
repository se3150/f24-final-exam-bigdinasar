from behave import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import time

@when('I enter a message about goblins')
def there_is_a_field_with_id_letters(context):
    try:
        # Locate the span element using its class name
        a = context.behave_driver.find_element(By.ID, "letters")

        # Clear any existing text in the input element
        a.clear()
        
        # Enter the number 2 into the input element
        a.send_keys("goblins are good")

        time.sleep(3)

    except NoSuchElementException:
        assert False, "No such elements were found on the page."
    except Exception as e:
        assert False, f"An unexpected error occurred: {str(e)}"

@when('I click the shift amount dropdown')
def there_is_a_field_with_id_letters(context):
    try:
        # Locate the span element using its class name
        s = context.behave_driver.find_element(By.ID, "shift-amount")
        
        # Enter the number 2 into the input element
        s.click()

        time.sleep(3)

    except NoSuchElementException:
        assert False, "No such elements were found on the page."
    except Exception as e:
        assert False, f"An unexpected error occurred: {str(e)}"

@when('I click 1')
def there_is_a_field_with_id_letters(context):
    try:
        # Locate the span element using its class name
        shifts = context.behave_driver.find_element(By.TAG_NAME, "option")

        target_shift = next(shift for shift in shifts if 1 in link.get_value("option"))
        
        # Enter the number 2 into the input element
        target_shift.click()

        time.sleep(3)

    except NoSuchElementException:
        assert False, "No such elements were found on the page."
    except Exception as e:
        assert False, f"An unexpected error occurred: {str(e)}"

@when('I hit submit')
def encode(context):
    try:
        # Locate the span element using its class name
        s = context.behave_driver.find_element(By.ID, "submit")
        
        # Enter the number 2 into the input element
        a.click()

        time.sleep(3)

    except NoSuchElementException:
        assert False, "No such elements were found on the page."
    except Exception as e:
        assert False, f"An unexpected error occurred: {str(e)}"

@then('I expect to there to be a field with goblin words')
def there_is_a_field_with_id_letters(context):
    try:
        # Locate the span element using its class name
        d = context.behave_driver.find_element(By.ID, "decoded_message")

        assert d.text == "goblins are good"


    except NoSuchElementException:
        assert False, "No such elements were found on the page."
    except Exception as e:
        assert False, f"An unexpected error occurred: {str(e)}"
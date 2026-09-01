from selenium.webdriver.common.by import By
FIRST_NAME = (By.ID,"first-name")
LAST_NAME = (By.ID,"last-name")
POSTAL_CODE = (By.XPATH,"//input[@id='postal-code']")
CONTINUE_BTN = (By.ID,"continue")
FINISH_BTN = (By.ID,"finish")
CONFIRMATION_MSG = (By.CLASS_NAME,"complete-header")
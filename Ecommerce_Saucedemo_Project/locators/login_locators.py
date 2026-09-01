from selenium.webdriver.common.by import By

USERNAME = (By.ID,"user-name")
PASSWORD = (By.ID,"password")
LOGIN_BTN = (By.XPATH,"//input[@type='submit']")
ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest
import time
from selenium.webdriver.common.by import By

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestWSB(unittest.TestCase):

    LOGIN_BUTTON = "ico-login"

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)

    def test_kurs_invalid_login(self):
        self.driver.get("http://demowebshop.tricentis.com/")
        self.driver.find_element(By.CLASS_NAME, self.LOGIN_BUTTON).click()
        self.driver.find_element(By.ID, "Email").send_keys("zuzanna#jakismail.ca")
        self.driver.find_element(By.ID, "Password").send_keys("dowolnehaslo")
        self.driver.find_element(By.ID, "RememberMe").click()
        WebDriverWait(self.driver, timeout=2).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "field-validation-error"),
                                                                                     "Please enter a valid email address."))

        time.sleep(5)

    def tearDown(self) -> None:
        self.driver.close()
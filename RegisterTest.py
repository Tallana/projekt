from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest
import time
from selenium.webdriver.common.by import By

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class WSBTest(unittest.TestCase):

    REGISTER_BUTTON = "ico-register"

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)

    def test_kurs_valid_registration(self):
        self.driver.get("http://demowebshop.tricentis.com/")
        self.driver.find_element(By.CLASS_NAME, self.REGISTER_BUTTON).click()
        self.driver.find_element(By.ID, "gender-female").click()
        self.driver.find_element(By.ID, "FirstName").send_keys("Zuzanna")
        self.driver.find_element(By.ID, "LastName").send_keys("Kowalska")
        self.driver.find_element(By.ID, "Email").send_keys("costamktostamgdziestam@surykatka.jedenziemniak")
        self.driver.find_element(By.ID, "Password").send_keys("Zuzanna1234")
        self.driver.find_element(By.ID, "ConfirmPassword").send_keys("Zuzanna1234")
        self.driver.find_element(By.CLASS_NAME, "register-next-step-button").click()
        self.driver.find_element(By.CLASS_NAME, "register-continue-button").click()

        time.sleep(5)

    def tearDown(self) -> None:
        self.driver.close()
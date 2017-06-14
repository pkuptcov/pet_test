# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Cart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://petrovich.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_cart(self):
        driver = self.driver
        driver.find_element_by_css_selector("span.short__fixed").click()
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "span.radio_input"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_link_text(u"Удалить").click()
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, u"input[placeholder=\"•••••••\"]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_css_selector(u"input[placeholder=\"•••••••\"]").clear()
        driver.find_element_by_css_selector(u"input[placeholder=\"•••••••\"]").send_keys("111111")
        driver.find_element_by_css_selector(u"button:contains('Пересчитать')").click()
        driver.find_element_by_css_selector("button[ng-click='totalCtrl.goToOrdering()']").click()
        for i in range(60):
            try:
                if re.search(r"^Введите адрес доставки [\s\S]*$", driver.find_element_by_css_selector("p.delivery_form_step_header").text): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
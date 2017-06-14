# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Order(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://petrovich.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_order(self):
        driver = self.driver
        driver.find_element_by_name("base").click()
        driver.find_element_by_name("delivery_pay").click()
        driver.find_element_by_css_selector("[ng-model=\"orderingSelfCtrl.order.userEmail\"]").clear()
        driver.find_element_by_css_selector("[ng-model=\"orderingSelfCtrl.order.userEmail\"]").send_keys("propetrovich@mail.ru")
        driver.find_element_by_css_selector("[ng-model=\"orderingSelfCtrl.order.userPhone\"]").clear()
        driver.find_element_by_css_selector("[ng-model=\"orderingSelfCtrl.order.userPhone\"]").send_keys("+7 (111) 111-11-11")
        driver.find_element_by_css_selector("textarea[ng-model='orderingSelfCtrl.order.userComment']").clear()
        driver.find_element_by_css_selector("textarea[ng-model='orderingSelfCtrl.order.userComment']").send_keys(u"тест")
        driver.find_element_by_css_selector("input[ng-click=\"orderingSelfCtrl.make($event)\"]").click()
        for i in range(60):
            try:
                if u"Спасибо за покупку!" == driver.find_element_by_css_selector("p.thanks__big-text").text: break
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

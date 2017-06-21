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
        driver.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.deliveryAddress\"]").clear()
        driver.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.deliveryAddress\"]").send_keys("Россия, Санкт-Петербург, Благодатная улица, 6")
        driver.find_element_by_xpath("(//input[@name='delivery_day'])[3]").click()
        driver.find_element_by_css_selector("label:contains('Стандартная доставка')").click()
        Select(driver.find_element_by_xpath("//div[@id='tab_delivery']/ol/li[3]/div/ul/li[2]/div/select")).select_by_visible_text("23:30 – 03:30")
        driver.find_element_by_name("delivery_pay").click()
        driver.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.userEmail\"]").clear()
        driver.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.userEmail\"]").send_keys("propetrovich@mail.ru")
        driver.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.userPhone\"]").clear()
        driver.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.userPhone\"]").send_keys("+7 (111) 111-11-11")
        driver.find_element_by_name("user_name").clear()
        driver.find_element_by_name("user_name").send_keys("Тест")
        driver.find_element_by_css_selector("textarea[ng-model='orderDeliveryCtrl.order.userComment']").clear()
        driver.find_element_by_css_selector("textarea[ng-model='orderDeliveryCtrl.order.userComment']").send_keys("тест")
        driver.find_element_by_css_selector("input[ng-click=\"orderDeliveryCtrl.make($event)\"]").click()
        for i in range(60):
            try:
                if "Спасибо за покупку!" == driver.find_element_by_css_selector("p.thanks__big-text").text: break
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

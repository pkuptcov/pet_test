# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class delivery_auth(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920, 1080)
        self.driver.implicitly_wait(30)
        self.base_url = "https://petrovich.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_regress(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Вход").click()
        driver.find_element_by_id("mainPetrovichLogin_login").clear()
        driver.find_element_by_id("mainPetrovichLogin_login").send_keys("xigekuba@p33.org")
        driver.find_element_by_id("mainPetrovichLogin_password").clear()
        driver.find_element_by_id("mainPetrovichLogin_password").send_keys("111111")
        driver.find_element_by_css_selector("div.form_row [type=submit]").click()
        for i in range(60):
            try:
                if self.is_element_present(By.LINK_TEXT, "test"): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")
        driver.find_element_by_id("query").clear()
        driver.find_element_by_id("query").send_keys("ондулин гвоздь")
        time.sleep(5)
        driver.find_element_by_css_selector("form#search [type=submit]").click()
        driver.find_element_by_css_selector("div.stepper-arrow.up.unit--step").click()
        driver.find_element_by_css_selector("[data-product-code='101845']").click()
        driver.find_element_by_css_selector("div.head_basket_wrapper").click()
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "span.radio_input"): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")
        driver.find_element_by_link_text("Удалить").click()
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "input[placeholder=\"•••••••\"]"): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")
        driver.find_element_by_css_selector("input[placeholder=\"•••••••\"]").clear()
        driver.find_element_by_css_selector("input[placeholder=\"•••••••\"]").send_keys("111111")
        driver.find_element_by_css_selector("button[ng-click='totalCtrl.addCard()']").click()
        driver.find_element_by_css_selector("button[ng-click='totalCtrl.goToOrdering()']").click()
        for i in range(60):
            try:
                if re.search(r"^Введите адрес доставки [\s\S]*$",
                             driver.find_element_by_css_selector("p.delivery_form_step_header").text): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")
        driver.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.deliveryAddress\"]").clear()
        driver.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.deliveryAddress\"]").send_keys(
            "Россия, Санкт-Петербург, Благодатная улица, 6")
        driver.find_element_by_xpath("(//input[@name='delivery_day'])[3]").click()
        driver.find_element_by_css_selector("[ng-change=\"orderDeliveryCtrl.deliveryTypeChange('standard')\"]").click()
        #Select(driver.find_element_by_xpath("//div[@id='tab_delivery']/ol/li[3]/div/ul/li[2]/div/select")).select_by_visible_text("23:30 – 03:30")
        time.sleep(1)
        driver.find_element_by_css_selector("option[value='С2330До0330']").click()
        driver.find_element_by_name("delivery_pay").click()
        driver.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.userEmail\"]").clear()
        driver.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.userEmail\"]").send_keys(
            "propetrovich@mail.ru")
        driver.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.userPhone\"]").clear()
        driver.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.userPhone\"]").send_keys(
            "+7 (111) 111-11-11")
        driver.find_element_by_name("user_name").clear()
        driver.find_element_by_name("user_name").send_keys("Тест")
        driver.find_element_by_css_selector("textarea[ng-model='orderDeliveryCtrl.order.userComment']").clear()
        driver.find_element_by_css_selector("textarea[ng-model='orderDeliveryCtrl.order.userComment']").send_keys(
            "тест")
        driver.find_element_by_css_selector("input[ng-click=\"orderDeliveryCtrl.make($event)\"]").click()
        for i in range(60):
            try:
                if "Спасибо за покупку!" == driver.find_element_by_css_selector("p.thanks__big-text").text: break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")
        driver.find_element_by_css_selector("a.auth_user_link").click()
        driver.find_element_by_link_text("Выход").click()
        for i in range(60):
            try:
                if self.is_element_present(By.LINK_TEXT, "Вход"): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
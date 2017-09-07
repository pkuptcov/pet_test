# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

        # Подключение вебдрайвера и конфиг окружения
class ur_delivery_non_auth(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://pet.beta.kluatr.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True

        # Переход на сайт
    def test_regress(self):
        driver = self.driver
        driver.get(self.base_url + "/")

        # Поиск товара по сайту
        driver.find_element_by_id("query").send_keys("ондулин гвоздь")
        driver.find_element_by_css_selector("form#search [type=submit]").click()

        # Увеличение товара в листинге выдачи поиска
        driver.find_element_by_css_selector("div.stepper-arrow.up.unit--step").click()
        driver.find_element_by_css_selector("[data-product-code='101846']").click()

        # Переход в корзину
        driver.find_element_by_css_selector("div.head_basket_wrapper").click()

        # Выбор вкладки юридического лица
        driver.find_element_by_xpath("//a[contains(text(),'Юридическое лицо')]").click()

        # Нажимаем оформить
        driver.find_element_by_css_selector("button[ng-click='totalCtrl.goToOrdering()']").click()

        # Страница оформления заказа
        driver.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.deliveryAddress\"]").send_keys(
            "Россия, Санкт-Петербург, Благодатная улица, 6")
        driver.find_element_by_xpath("(//input[@name='delivery_day'])[3]").click()
        driver.find_element_by_css_selector("[ng-change=\"orderDeliveryCtrl.deliveryTypeChange('standard')\"]").click()
        time.sleep(1)
        driver.find_element_by_css_selector("option[value='С2330До0330']").click()
        driver.find_element_by_css_selector("input[placeholder=\"Название\"]").clear()
        driver.find_element_by_css_selector("input[placeholder=\"Название\"]").send_keys("Тест")
        driver.find_element_by_css_selector("input[placeholder=\"ИНН\"]").clear()
        driver.find_element_by_css_selector("input[placeholder=\"ИНН\"]").send_keys("1231231231")
        driver.find_element_by_css_selector("input[placeholder=\"КПП\"]").clear()
        driver.find_element_by_css_selector("input[placeholder=\"КПП\"]").send_keys("123123123")
        driver.find_element_by_css_selector("input[value=\"legalNonCash\"]").click()
        driver.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.userEmail\"]").clear()
        driver.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.userEmail\"]").send_keys(
            "propetrovich@mail.ru")
        driver.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.userPhone\"]").clear()
        driver.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.userPhone\"]").send_keys(
            "(111) 111-11-11")
        driver.find_element_by_name("user_name").clear()
        driver.find_element_by_name("user_name").send_keys("Тест")
        driver.find_element_by_css_selector("textarea[ng-model='orderDeliveryCtrl.order.userComment']").send_keys(
            "тест")
        driver.find_element_by_css_selector("input[ng-click=\"orderDeliveryCtrl.make($event)\"]").click()

        # Страница спасибо за покупку и переход в личный кабинет
        driver.find_element_by_css_selector("a.thanks__lk-link").click()

        # Проверка оформленного заказа
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.order__id"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "p.__info__title"))

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
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

        # Подключение вебдрайвера и конфиг окружения
class self_non_auth(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://petrovich.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True

        # Переход на страницу сайта
    def test_city_change(self):
        driver = self.driver
        driver.get(self.base_url + "/")

        # По умолчанию в СПБ
        driver.find_element_by_link_text("Вход").click()
        driver.find_element_by_id("mainPetrovichLogin_login").clear()
        driver.find_element_by_id("mainPetrovichLogin_login").send_keys("xigekuba@p33.org")
        driver.find_element_by_id("mainPetrovichLogin_password").clear()
        driver.find_element_by_id("mainPetrovichLogin_password").send_keys("111111")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("test").click()
        driver.find_element_by_link_text("Выход").click()
        time.sleep(1)

        # Выбор Москвы
        driver.find_element_by_css_selector("div.top_region").click()
        time.sleep(1)
        driver.find_element_by_link_text("Москва").click()
        driver.find_element_by_link_text("Вход").click()
        driver.find_element_by_id("mainPetrovichLogin_login").clear()
        driver.find_element_by_id("mainPetrovichLogin_login").send_keys("xigekuba@p33.org")
        driver.find_element_by_id("mainPetrovichLogin_password").clear()
        driver.find_element_by_id("mainPetrovichLogin_password").send_keys("111111")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("test").click()
        driver.find_element_by_link_text("Выход").click()
        time.sleep(1)

        # Выбор Великого Новгорода
        driver.find_element_by_css_selector("div.top_region").click()
        time.sleep(1)
        driver.find_element_by_link_text("Великий Новгород").click()
        driver.find_element_by_link_text("Вход").click()
        driver.find_element_by_id("mainPetrovichLogin_login").clear()
        driver.find_element_by_id("mainPetrovichLogin_login").send_keys("xigekuba@p33.org")
        driver.find_element_by_id("mainPetrovichLogin_password").clear()
        driver.find_element_by_id("mainPetrovichLogin_password").send_keys("111111")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("test").click()
        driver.find_element_by_link_text("Выход").click()
        time.sleep(1)

        # Выбор Выборга
        driver.find_element_by_css_selector("div.top_region").click()
        time.sleep(1)
        driver.find_element_by_link_text("Выборг").click()
        driver.find_element_by_link_text("Вход").click()
        driver.find_element_by_id("mainPetrovichLogin_login").clear()
        driver.find_element_by_id("mainPetrovichLogin_login").send_keys("xigekuba@p33.org")
        driver.find_element_by_id("mainPetrovichLogin_password").clear()
        driver.find_element_by_id("mainPetrovichLogin_password").send_keys("111111")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("test").click()
        driver.find_element_by_link_text("Выход").click()
        time.sleep(1)

        # Выбор Луги
        driver.find_element_by_css_selector("div.top_region").click()
        time.sleep(1)
        driver.find_element_by_link_text("Луга").click()
        driver.find_element_by_link_text("Вход").click()
        driver.find_element_by_id("mainPetrovichLogin_login").clear()
        driver.find_element_by_id("mainPetrovichLogin_login").send_keys("xigekuba@p33.org")
        driver.find_element_by_id("mainPetrovichLogin_password").clear()
        driver.find_element_by_id("mainPetrovichLogin_password").send_keys("111111")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("test").click()
        driver.find_element_by_link_text("Выход").click()
        time.sleep(1)

        # Выбор Кингисеппа
        driver.find_element_by_css_selector("div.top_region").click()
        time.sleep(1)
        driver.find_element_by_link_text("Кингисепп").click()
        driver.find_element_by_link_text("Вход").click()
        driver.find_element_by_id("mainPetrovichLogin_login").clear()
        driver.find_element_by_id("mainPetrovichLogin_login").send_keys("xigekuba@p33.org")
        driver.find_element_by_id("mainPetrovichLogin_password").clear()
        driver.find_element_by_id("mainPetrovichLogin_password").send_keys("111111")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("test").click()
        driver.find_element_by_link_text("Выход").click()
        time.sleep(1)

        # Выбор Петрозаводска
        driver.find_element_by_css_selector("div.top_region").click()
        time.sleep(1)
        driver.find_element_by_link_text("Петрозаводск").click()
        driver.find_element_by_link_text("Вход").click()
        driver.find_element_by_id("mainPetrovichLogin_login").clear()
        driver.find_element_by_id("mainPetrovichLogin_login").send_keys("xigekuba@p33.org")
        driver.find_element_by_id("mainPetrovichLogin_password").clear()
        driver.find_element_by_id("mainPetrovichLogin_password").send_keys("111111")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("test").click()
        driver.find_element_by_link_text("Выход").click()
        time.sleep(1)

        # Выбор Твери
        driver.find_element_by_css_selector("div.top_region").click()
        time.sleep(1)
        driver.find_element_by_link_text("Тверь").click()
        driver.find_element_by_link_text("Вход").click()
        driver.find_element_by_id("mainPetrovichLogin_login").clear()
        driver.find_element_by_id("mainPetrovichLogin_login").send_keys("xigekuba@p33.org")
        driver.find_element_by_id("mainPetrovichLogin_password").clear()
        driver.find_element_by_id("mainPetrovichLogin_password").send_keys("111111")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("test").click()
        driver.find_element_by_link_text("Выход").click()
        time.sleep(1)

        # Проверка выхода из ЛК
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Вход"))

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

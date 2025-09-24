import allure
from project.data import Data
from selenium.webdriver.common.by import By
from project.pages.base_page import BasePage
from project.locators.call_taxi_page_locators import CallTaxiPageLocators




class ElementAlreadySelected(Exception):
    pass


class CallTaxiPage(BasePage):

    @allure.step("Получение списка видов такси по ТЗ")
    def is_get_6_taxi_titles(self):
        try:
            elements = self.find_elements_with_wait(CallTaxiPageLocators.ELEMENTS_TAXI_TITLE)
            any(el.text in Data.EXPECTED_TAXI_TITLE for el in elements)
            return True
        except ElementAlreadySelected:
            return False

    @allure.step("Есть ли активное окно в одном из 6 видов такси")
    def is_one_active_taxi_title(self):
        elements = self.find_elements_with_wait(CallTaxiPageLocators.ELEMENTS_TAXI_TITLE)
        active_element = self.find_element_with_wait(CallTaxiPageLocators.ACTIVE_TAXI_TITLE)
        for el in elements:
            locator = f"//div[text()='{el.text}']"
            try:
                active_element.find_element(By.XPATH, locator)
                condition = True
            except ElementAlreadySelected:
                print(f"Тариф {el.text} неактивный")
                condition = False
        return condition

    def modal_window_with_description_tarif(self, taxi_title):
        locator = (By.XPATH, f'//div[@class="tcard-title" and text()="{taxi_title}"]')
        try:
            self.click_on_element(locator)
        except ElementAlreadySelected(f"Элемент {taxi_title} уже выбран"):
            pass
        taxi_info = self.find_element_with_wait(CallTaxiPageLocators.TAXI_INFO)
        self.hover_at_element(taxi_info)
        _ = self.find_element_with_wait(CallTaxiPageLocators.TARIF_NAME)
        text_from_tarif_name = self.get_text_from_element(CallTaxiPageLocators.TARIF_NAME)
        self.hover_at_element(taxi_info)
        _ = self.find_element_with_wait(CallTaxiPageLocators.TARIF_DESCRIPTION)
        text_from_tarif_description = self.get_text_from_element(CallTaxiPageLocators.TARIF_DESCRIPTION)
        actual_tarif_name_description = f'{text_from_tarif_name} - {text_from_tarif_description}'
        return actual_tarif_name_description

    @allure.step("Под тарифами отображается блок с полями Телефон, Способ оплаты, Комментарий водителю, Требования к заказу \
    Заказ тарифа Такси.")
    def is_visible_block_of_order(self, locator, block):
        try:
            condition = self.check_element_visible(locator)
        except ElementAlreadySelected:
            print(f"Не отображается {block}")
            condition = False
        return condition

    @allure.step("Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать - \
    Появляется окно ожидания машины (проверить элементы по ТЗ)")
    def is_check_window_waiting_auto(self, locator):
        try:
            self.click_on_element(CallTaxiPageLocators.WORKING)
        except ElementAlreadySelected:
            pass
        self.scroll_to_element(CallTaxiPageLocators.RAIDER)
        self.click_on_element(CallTaxiPageLocators.RAIDER)
        self.scroll_to_element(CallTaxiPageLocators.LAPTOP_TABLE_TOGGLE)
        self.click_on_element(CallTaxiPageLocators.LAPTOP_TABLE_TOGGLE)
        self.click_on_element(CallTaxiPageLocators.BUTTON_ENTER_NUMBER_AND_ORDER)
        condition = self.check_element_visible(locator)
        return condition

    @allure.step("Дождаться окончания таймера поиска машины - Отображается окно совершенного заказа (проверить элементы по ТЗ)")
    def is_check_window_final_order(self, locator):
        self.long_waiting_to_invisible_element(CallTaxiPageLocators.TIMER)
        condition = self.check_element_visible(locator)
        return condition

    @allure.step("Имя водителя есть в списке имен")
    def is_check_driver_name(self):
        self.long_waiting_to_invisible_element(CallTaxiPageLocators.TIMER)
        self.find_element_with_wait(CallTaxiPageLocators.DRIVER_NAME)
        name = self.get_text_from_element(CallTaxiPageLocators.DRIVER_NAME)
        return name in Data.DRIVER_NAMES

    @allure.step("Сравниваем цену до и после заказа")
    def is_equel_price(self):
        text = self.get_text_from_element(CallTaxiPageLocators.PRICE_BEFORE_ORDER)
        price_before = text.split()[2]
        self.confirm_order_taxi()
        _ = self.is_check_window_waiting_auto(CallTaxiPageLocators.ORDER_DETAILS)
        self.click_on_element(CallTaxiPageLocators.ORDER_DETAILS)
        text = self.get_text_from_element(CallTaxiPageLocators.PRICE_AFTER_ORDER)
        text = text.split()[2]
        price_after = text.split('₽')[0]
        print(price_after)
        return price_before == price_after

    @allure.step("Нажимаем на кнопку Отменить")
    def is_click_cancel(self):
        _ = self.is_check_window_waiting_auto(CallTaxiPageLocators.TIMER)
        self.click_on_element(CallTaxiPageLocators.CANCEL)
        return self.waiting_to_invisible_element(CallTaxiPageLocators.MODAL_WAITING)


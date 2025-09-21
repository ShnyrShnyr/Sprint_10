import allure
from project.data import Data
from project.pages.base_page import BasePage
from project.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Возвращаем элементы точек отправления и назначения")
    def drawing_a_route(self):
        self.add_two_address(Data.LOCATION_1, Data.LOCATION_2)
        condition_1 = self.check_element_visible(MainPageLocators.FROM_FIELD)
        condition_2 = self.check_element_visible(MainPageLocators.TO_FIELD)
        return condition_1, condition_2

    @allure.step("Вводим адреса маршрута и проверяем отображение блока с выбором маршрута")
    def create_block_choice_way(self, list_locators_in_block):
        for i in list_locators_in_block:
            condition = self.check_element_visible(i)
            if condition == False:
                break
        return condition

    @allure.step("Забираем текст с 2х элементов блока с выбором маршрута")
    def get_elements_after_input_one_address(self):
        MainPageLocators.LOCATORS_OF_CHOICE.pop(-1)
        self.add_two_address(Data.LOCATION_1, Data.LOCATION_1)
        condition = self.create_block_choice_way(MainPageLocators.LOCATORS_OF_CHOICE)
        actual_text = self.get_list_text_from_elements(MainPageLocators.TYPE_AND_PRICE_DELIVERY, MainPageLocators.TRAVEL_TIME)
        return condition, actual_text

    @allure.step("Меняем выбор пути с быстрого на оптимальный и возвращаем ожидаемые и актуальные значения")
    def change_type_of_way(self):
        self.add_two_address(Data.LOCATION_1, Data.LOCATION_2)
        text_in_element_quick = self.get_list_text_from_elements(MainPageLocators.TYPE_AND_PRICE_DELIVERY, MainPageLocators.TRAVEL_TIME)
        self.click_on_element(MainPageLocators.OPTIMA)
        text_in_element_optima = self.get_list_text_from_elements(MainPageLocators.TYPE_AND_PRICE_DELIVERY, MainPageLocators.TRAVEL_TIME)
        actual_text_in_active_tab = self.get_text_from_element(MainPageLocators.ACTIVE_TAB)
        return text_in_element_quick, text_in_element_optima, actual_text_in_active_tab

    @allure.step("При нажатии на свой маршрут становятся активны разные виды транспорта")
    def change_transport_at_own(self):
        self.add_two_address(Data.LOCATION_1, Data.LOCATION_2)
        element_before = self.find_element_with_wait(MainPageLocators.OWN)
        self.click_on_element(MainPageLocators.OWN)
        element_after = self.find_element_with_wait(MainPageLocators.ACTIVE_TAB)
        if element_before == element_after:
            condition = True
        for i in MainPageLocators.LOCATORS_OF_TRANSPORT:
            condition = self.check_element_is_clickable(i)
            if condition == False:
                break
        return condition

    @allure.step("В быстром маршруте активна кнопка Вызвать такси")
    def active_order_button(self):
        self.add_two_address(Data.LOCATION_1, Data.LOCATION_2)
        condition = self.check_element_is_clickable(MainPageLocators.CALL_TAXI)
        return condition

    @allure.step("В тарифе Свой активна кнопка Забронировать")
    def active_confirmation(self):
        self.add_two_address(Data.LOCATION_1, Data.LOCATION_2)
        self.click_on_element(MainPageLocators.OWN)
        self.find_element_with_wait(MainPageLocators.TYPE_DRIVE)
        self.click_on_element(MainPageLocators.TYPE_DRIVE)
        self.find_element_with_wait(MainPageLocators.CONFIRMATION)
        condition = self.check_element_is_clickable(MainPageLocators.CONFIRMATION)
        return condition


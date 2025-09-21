import allure
import pytest
from project.data import Data
from project.locators.call_taxi_page_locators import CallTaxiPageLocators



class TestCallTaxiPage:
    @allure.title("Проверка наличия 6 видов тарифов по ТЗ")
    def test_is_get_6_taxi_titles(self, call_taxi_page):
        condition = call_taxi_page.is_get_6_taxi_titles()
        assert condition, "Не отображаются 6 видов тарифов по ТЗ"

    @allure.title("Проверка что один из тарифов активен")
    def test_is_one_active_taxi_title(self,call_taxi_page):
        condition = call_taxi_page.is_one_active_taxi_title()
        assert condition, "Нет активного тарифа"

    @pytest.mark.parametrize(
        'taxi_title, expected_tarif_description',
        [
            pytest.param(*Data.DATA_1, marks=pytest.mark.xfail(reason="У тарифа сонный описание от разговорчивый")),
            Data.DATA_2,
            pytest.param(*Data.DATA_3, marks=pytest.mark.xfail(reason="У тарифа разговорчивый описание от сонный")),
            Data.DATA_4,
            Data.DATA_5,
            Data.DATA_6
        ]
    )
    @allure.title("Проверка описания маршрута c названием {taxi_title}")
    def test_modal_window_with_description_tarif(self, call_taxi_page, taxi_title, expected_tarif_description):
        actual_tarif_description = call_taxi_page.modal_window_with_description_tarif(taxi_title)
        assert actual_tarif_description == expected_tarif_description, f"Тариф {taxi_title} имеет неправильное описание"

    @pytest.mark.parametrize(
        'locator, block',
        [
            [CallTaxiPageLocators.BLOCK_FOR_ORDER[0], Data.BLOCK_FOR_ORDER[0]],
            [CallTaxiPageLocators.BLOCK_FOR_ORDER[1], Data.BLOCK_FOR_ORDER[1]],
            [CallTaxiPageLocators.BLOCK_FOR_ORDER[2], Data.BLOCK_FOR_ORDER[2]],
            [CallTaxiPageLocators.BLOCK_FOR_ORDER[3], Data.BLOCK_FOR_ORDER[3]],
            [CallTaxiPageLocators.BLOCK_FOR_ORDER[4], Data.BLOCK_FOR_ORDER[4]]
        ]
    )
    @allure.title("Проверка блока заказа на наличие поля {block}")
    def test_is_visible_block_of_order(self, call_taxi_page, locator, block):
        condition = call_taxi_page.is_visible_block_of_order(locator, block)
        assert condition

    @pytest.mark.parametrize(
        'locator',
        (
            CallTaxiPageLocators.HEADER_OF_MODAL,
            CallTaxiPageLocators.TIMER,
            CallTaxiPageLocators.CANCEL,
            CallTaxiPageLocators.ORDER_DETAILS
        )
    )
    @allure.title("Проверка, что отображается элемент {locator} в окне Поиск машины")
    def test_is_check_window_waiting_auto(self, call_taxi_page, locator):
        assert call_taxi_page.is_check_window_waiting_auto(locator), f"Элемент {locator} не отображается"

    @pytest.mark.parametrize(
        'locator',
        [
            CallTaxiPageLocators.HEADER_OF_FINAL_MODAL,
            CallTaxiPageLocators.AUTO_NUMBER,
            CallTaxiPageLocators.AUTO_IMG,
            CallTaxiPageLocators.DRIVER_FOTO,
            CallTaxiPageLocators.DRIVER_RAITING,
            CallTaxiPageLocators.CANCEL,
            CallTaxiPageLocators.ORDER_DETAILS
        ]
    )
    @allure.title("Проверка, что отображается элемент {locator} в окне ожидания машины")
    def test_is_check_window_final_order(self,call_taxi_page, locator):
        _ = call_taxi_page.is_check_window_waiting_auto(CallTaxiPageLocators.HEADER_OF_MODAL)
        assert call_taxi_page.is_check_window_final_order(locator)

    @allure.title("Провека имен водителей")
    def test_is_check_driver_name(self, call_taxi_page):
        _ = call_taxi_page.is_check_window_waiting_auto(CallTaxiPageLocators.HEADER_OF_MODAL)
        assert call_taxi_page.is_check_driver_name()

    @allure.title("Проверка блока Еще")
    def test_is_equel_price(self, call_taxi_page_else):
        assert call_taxi_page_else.is_equel_price()

    @pytest.mark.xfail(reason="Баг-кнопка 'Отменить' не кликабельна")
    @allure.title("Проверка кнопки Отменить")
    def test_is_click_cancel(self, call_taxi_page):
        assert call_taxi_page.is_click_cancel()
import allure
from project.data import Data
from project.tests.conftest import main_page
from project.locators.main_page_locators import MainPageLocators



class TestMainPage:
    @allure.title("Проверка отображения 2х точек маршрута на карте")
    def test_drawing_a_route (self, main_page):
        condition_1, condition_2 = main_page.drawing_a_route()
        assert condition_1 ==True and condition_2 == True, "Не отображается одна или обе точки на карте"

    @allure.title("Проверка отображения блока заказа")
    def test_create_block_choice_way(self, main_page):
        main_page.add_two_address(Data.LOCATION_1,Data.LOCATION_2)
        condition = main_page.create_block_choice_way(MainPageLocators.LOCATORS_OF_CHOICE)
        assert condition == True, "Не отображается один из элементов блока заказа"

    @allure.title("Проверка отображения элементов 'Авто Бесплатно', 'В пути 0 мин.' при вводе одного адреса в оба поля")
    def test_get_elements_after_input_one_address(self, main_page):
        condition, actual_text = main_page.get_elements_after_input_one_address()
        assert condition == True and actual_text == Data.EXPECTED_TEXT, "Не отображается один из элементов блока заказа или Не совпадает текст элементов в блоке выбора маршрута"

    @allure.title("Проверка смены таба на 'Оптимальный' и изменение стоимости и времени поездки")
    def test_change_type_of_way(self, main_page):
        text_quick, text_optima, text_actual_in_active_tab = main_page.change_type_of_way()
        assert text_quick != text_optima and text_actual_in_active_tab == Data.EXPECTED_ACTIVE_TAB, "Не изменился текст после смены таба или не сменился сам таб на оптимальный"

    @allure.title("Проверка смены таба при выборе маршрута 'Свой' и на видах транспорта")
    def test_change_transport_at_own(self,main_page):
        condition = main_page.change_transport_at_own()
        assert condition == True, "Активный таб не сменился на 'Свой' или таб не устанавливается при клике на транспорт"

    @allure.title("Проверка активности кнопки Вызвать такси в быстром маршруте")
    def test_active_order_button(self,main_page):
        condition = main_page.active_order_button()
        assert condition == True, "Кнопка вызвать такси не активна на маршруте Быстрый"

    @allure.title("Проверка активности кнопки забронировать в маршруте свой транспорте Драйв")
    def test_active_confirmation(self,main_page):
        condition = main_page.active_confirmation()
        assert condition == True, "Кнопка Забронировать не активна в маршруте Свой и транспорте Драйв"


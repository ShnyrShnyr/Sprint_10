import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from project.locators.main_page_locators import MainPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,5)
        self.long_wait = WebDriverWait(self.driver, 40)


    @allure.step("Поиск элемента с ожиданием пока не будет виден")
    def find_element_with_wait(self, locator):
        self.wait.until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)


    @allure.step("Поиск элементов с ожиданием пока не будут видны все")
    def find_elements_with_wait(self, locator):
        self.wait.until(ec.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step("Ожидание пока модальное окно перестанет быть видимым")
    def waiting_to_invisible_element(self, locator):
        self.wait.until(ec.invisibility_of_element_located(locator))

    @allure.step("Длинное ожидание пока модальное окно перестанет быть видимым")
    def long_waiting_to_invisible_element(self, locator):
        self.long_wait.until(ec.invisibility_of_element_located(locator))


    @allure.step("Переход по URL")
    def go_to_url(self, url):
        self.driver.get(url)


    @allure.step("Ввести текст в поле ввода")
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)


    @allure.step("Получить текст из элемента")
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        text = element.text
        return text

    @allure.step("Получить список с текстом из 2х элементов")
    def get_list_text_from_elements(self, locator_1, locator_2):
        actual_text = [self.get_text_from_element(locator_1),
                   self.get_text_from_element(locator_2)]
        return actual_text

    @allure.step("Проверить что элемент видимый")
    def check_element_visible(self, locator):
        """
        Проверяет, что элемент виден.
        Возвращает True/False, не бросает исключение.
        locator – кортеж (By.XPATH, '…')
        """
        try:
            _ = self.find_element_with_wait(locator)
            return True
        except TimeoutException:
            return False

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator):
        self.find_element_with_wait(locator).click()


    @allure.step('Проверить кликабельность элемента')
    def check_element_is_clickable(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator))
        return True


    @allure.step("Вводим адреса отправления и назначения")
    def add_two_address(self, from_address, to_address):
        self.add_text_to_element(MainPageLocators.FROM_FIELD, from_address)
        self.add_text_to_element(MainPageLocators.TO_FIELD, to_address)

    @allure.step("Навести на элемент")
    def hover_at_element(self, element):
        action = ActionChains(self.driver).move_to_element(element)
        action.perform()

    @allure.step("Проскролить до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Нажать на элемент Заказать такси")
    def confirm_order_taxi(self):
        self.click_on_element(MainPageLocators.CALL_TAXI)

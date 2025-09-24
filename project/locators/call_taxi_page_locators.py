from selenium.webdriver.common.by import By


class CallTaxiPageLocators:
    ACTIVE_TAXI_TITLE = By.XPATH, '//div[@class="tcard active"]'
    ELEMENTS_TAXI_TITLE = By.XPATH, '//div[@class="tcard-title"]'
    CHECK_ACTIVE = By.XPATH, '//div[@class="tcard active"]/div[text()="{taxi_title}"]'
    TAXI_INFO = By.XPATH, '//div[@class="tcard active"]/button'
    TARIF_NAME = By.CSS_SELECTOR, 'div.tcard.active div.i-title'
    TARIF_DESCRIPTION = By.CSS_SELECTOR, 'div.tcard.active div.i-dPrefix'
    CALL_TAXI = By.XPATH, '//button[text()="Вызвать такси"]'

    PHONE = By.XPATH, '//div[text()="Телефон"]'
    PAYMENT_METHOD = By.XPATH, '//div[@class="pp-button filled"]'
    COMMENT = By.XPATH, '//label[text()="Комментарий водителю..."]'
    REQUIREMENTS_FOR_ORDER = By.XPATH, '//div[@class="reqs-header"]'
    BUTTON_CREATE_ORDER = By.XPATH, '//button[@class="smart-button"]'
    BLOCK_FOR_ORDER = [PHONE,PAYMENT_METHOD,COMMENT,REQUIREMENTS_FOR_ORDER,BUTTON_CREATE_ORDER]

    WORKING = By.XPATH, '//div[@class="tcard-title" and text()="Рабочий"]'
    RAIDER = By.XPATH, '//div[@class="reqs"]'
    LAPTOP_TABLE_TOGGLE = By.XPATH,'//span[@class="slider round"]'
    BUTTON_ENTER_NUMBER_AND_ORDER = By.XPATH, '//span[text()="Ввести номер и заказать"]'

    MODAL_WAITING = By.XPATH, '//div[@class="order-body"]'
    CANCEL = By.XPATH, '//button/following-sibling::div[text()="Отменить"]'
    ORDER_DETAILS = By.XPATH,'//div[text()="Детали"]/parent::div'
    TIMER = By.XPATH, '//div[@class="order-header-time"]'
    HEADER_OF_MODAL = By.XPATH, '//div[@class="order-header-title" and text()="Поиск машины"]'

    HEADER_OF_FINAL_MODAL = By.XPATH, '//div[contains(@class,"order-header-content") and contains(normalize-space(.)," мин. и приедет")]'
    AUTO_NUMBER = By.CSS_SELECTOR, 'div.number'
    AUTO_IMG = By.XPATH, '//img [@alt="Car"]'
    DRIVER_NAME = By.XPATH, '//div[@class="order-button"]/following-sibling::div'
    DRIVER_FOTO = By.XPATH, '//div[contains(@class, "rating")]/following-sibling::img[@alt="close"]'
    DRIVER_RAITING = By.XPATH, '//div[@class="order-btn-rating"]'
    PRICE_AFTER_ORDER = By.XPATH, '//div[text()="Еще про поездку"]/following-sibling::div'
    PRICE_BEFORE_ORDER = By.XPATH, '//div[@class="text"]'
'''Окно совершенного заказа Такси: 
Заголовок: n мин. и приедет >
Номер автомобиля и картинка тарифа в правом верхнем углу
Блок с информацией о водителе: Имя, фото, рейтинг в правом верхнем углу фото
Кнопки: Отменить, Детали'''
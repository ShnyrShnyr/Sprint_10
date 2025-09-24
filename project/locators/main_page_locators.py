from selenium.webdriver.common.by import By


class MainPageLocators:

    FROM_FIELD = By.XPATH, '//input[@id="from"]'
    TO_FIELD = By.XPATH, '//input[@id="to"]'
    FROM_DOT = By.XPATH, '//ymaps[contains(@class,"ff3333")]'
    TO_DOT = By.XPATH, '//ymaps[contains(@class,"4296ea")]'

    OPTIMA = By.XPATH,'//div[text()="Оптимальный"]'
    QUICK = By.XPATH, '//div[text()="Быстрый"]'
    TYPE_AND_PRICE_DELIVERY = By.XPATH,'//div[@class="text"]'
    TRAVEL_TIME = By.XPATH, '//div[@class="duration"]'
    CALL_TAXI = By.XPATH, '//button[text()="Вызвать такси"]'
    LOCATORS_OF_CHOICE = [OPTIMA, QUICK, TYPE_AND_PRICE_DELIVERY, TRAVEL_TIME, CALL_TAXI]

    OWN = By.XPATH, '//div[text()="Свой"]'
    ACTIVE_TAB = By.XPATH, '//div[@class="mode active"]'
    TYPE_CAR = By.XPATH, '//div/img[contains(@src,"car.")]'
    TYPE_WALK = By.XPATH, '//img[contains(@src,"walk")]'
    TYPE_TAXI = By.XPATH, '//img[contains(@src,"taxi")]'
    TYPE_BIKE = By.XPATH, '//img[contains(@src,"bike")]'
    TYPE_SCOOTER = By.XPATH, '//img[contains(@src,"scooter")]'
    TYPE_DRIVE = By.XPATH, '//img[contains(@src,"drive")]'
    LOCATORS_OF_TRANSPORT = [TYPE_WALK, TYPE_TAXI, TYPE_BIKE, TYPE_SCOOTER, TYPE_DRIVE, TYPE_CAR]
    TYPE_ACTIVE = By.XPATH, '//img[contains(@src,"-active")]'
    CONFIRMATION = By.XPATH,'//button[text()="Забронировать"]'



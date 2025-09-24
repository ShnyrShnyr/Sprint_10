class Data:
    MAIN_PAGE_URL = 'https://ez-route.stand.praktikum-services.ru/'
    LOCATION_1 = 'Хамовнический вал, 34'
    LOCATION_2 = 'Зубовский бульвар, 37'
    EXPECTED_TEXT = ['Авто Бесплатно', 'В пути 0 мин.']
    EXPECTED_ACTIVE_TAB = 'Оптимальный'
    EXPECTED_TAXI_TITLE = ['Сонный', 'Отпускной', 'Разговорчивый', 'Утешительный', 'Глянцевый', 'Рабочий']
    EXPECTED_DESCRIPTION_TAXI = ['Сонный - Для тех, кто не выспался',
                                 'Отпускной - Если пришла пора отдохнуть',
                                 'Разговорчивый - Если мысли не выходят из головы',
                                 'Утешительный - Если хочется свернуться калачиком',
                                 'Глянцевый - Если нужно блистать',
                                 'Рабочий - Для деловых особ, которых отвлекают']
    DATA_1 = EXPECTED_TAXI_TITLE[0], EXPECTED_DESCRIPTION_TAXI[0]
    DATA_2 = EXPECTED_TAXI_TITLE[1], EXPECTED_DESCRIPTION_TAXI[1]
    DATA_3 = EXPECTED_TAXI_TITLE[2], EXPECTED_DESCRIPTION_TAXI[2]
    DATA_4 = EXPECTED_TAXI_TITLE[3], EXPECTED_DESCRIPTION_TAXI[3]
    DATA_5 = EXPECTED_TAXI_TITLE[4], EXPECTED_DESCRIPTION_TAXI[4]
    DATA_6 = EXPECTED_TAXI_TITLE[5], EXPECTED_DESCRIPTION_TAXI[5]

    BLOCK_FOR_ORDER = ['Телефон', 'Способ оплаты', 'Комментарий водителю', 'Требования к заказу', 'Заказ тарифа Такси']

    DRIVER_NAMES = ['Алексей','Пётр','Михаил','Григорий','Аркадий']





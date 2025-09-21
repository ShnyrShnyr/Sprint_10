import pytest
from project.data import Data
from selenium import webdriver
from project.pages.main_page import MainPage
from project.pages.call_taxi_page import CallTaxiPage



@pytest.fixture(scope="function")
def driver():
    drv = webdriver.Chrome()
    drv.maximize_window()
    yield drv
    drv.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.go_to_url(Data.MAIN_PAGE_URL)
    return page

@pytest.fixture
def call_taxi_page(driver, main_page):
    _ = main_page
    page = CallTaxiPage(driver)
    page.add_two_address(Data.LOCATION_1, Data.LOCATION_2)
    page.confirm_order_taxi()
    return page

@pytest.fixture
def call_taxi_page_else(driver, main_page):
    page_main = main_page
    page_main.add_two_address(Data.LOCATION_1, Data.LOCATION_2)
    page_call = CallTaxiPage(driver)
    return page_call


from types import TracebackType
from typing import Type
from selenium import webdriver
from selenium.webdriver.common.by import By
import booking.constants as const
import time

class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        # using options to keep chrome open after testing
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.teardown = teardown
        super(Booking, self).__init__(options=options)
        # wait at most 15s to find the element
        # it will apply to each method
        self.implicitly_wait(15)
        self.maximize_window()

    # when context manager blcok reaches the end
    # this __exit__ function will be called automatically
    # and webdriver.quit() will be called
    def __exit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, traceback: TracebackType | None):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def close_signin_popup(self):
        close_btn = self.find_element(By.CSS_SELECTOR, "button[aria-label='Dismiss sign-in info.']")
        close_btn.click()
    
    def search_place_togo(self, place):
        search_place_input = self.find_element(By.ID, ":rh:")
        search_place_input.send_keys(place)
        time.sleep(1)
        first_result = self.find_element(By.ID, "autocomplete-result-0")
        first_result.click()

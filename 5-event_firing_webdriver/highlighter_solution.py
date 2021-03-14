from selenium.webdriver.support.events import AbstractEventListener

from time import sleep

class highlighter_solution(AbstractEventListener):

    def before_click(self, element, driver):
        driver.execute_script('arguments[0].style.backgroundColor = "#FDFF47"', element)
        sleep(0.25)

    def after_click(self, element, driver):
        sleep(0.25)
        driver.execute_script('arguments[0].style.backgroundColor = ""', element)

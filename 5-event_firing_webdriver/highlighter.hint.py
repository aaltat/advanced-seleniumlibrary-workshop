# Using MyListener.py as a model create a listener class to highlight the element before an after clicking
#
# Here we can use
#     driver.execute_script('arguments[0].style.backgroundColor = "#FDFF47"', element)
# to highlight the element and
#     driver.execute_script('arguments[0].style.backgroundColor = ""', element)
# to "un-highlight" it again

# Helpful addition
# use the sleep method from the time module to put in some time after highlighting and before
# un highlighting so you can see the effect
from selenium.webdriver.support.events import AbstractEventListener

from time import sleep

class ???(AbstractEventListener):

    def ???(self, element, driver):
        driver.execute_script('arguments[0].style.backgroundColor = "#FDFF47"', element)
        sleep(0.25)

    def ???(self, element, driver):
        sleep(0.25)
        driver.execute_script('arguments[0].style.backgroundColor = ""', element)

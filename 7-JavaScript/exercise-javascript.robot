*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Using Javascript To Hide Floating Menu
    Open Browser    http://the-internet.herokuapp.com/floating_menu    Chrome
    # Exercise:
    #   Task 1 - Use Javascript to hide the menu
    #   Task 2 - Prove that the menu was there, no longer there, and back again
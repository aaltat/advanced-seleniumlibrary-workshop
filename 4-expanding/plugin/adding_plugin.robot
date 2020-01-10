*** Settings ***
Library    SeleniumLibrary    plugins=${CURDIR}/MyPlugin.py

*** Test Cases ***
Adding New Keyword From Class
    [Tags]    2
    ${text} =    New Keyword
    Should Be Equal    ${text}    New Keyword

Overwriting Exsisting Keyword
    [Tags]    2
    ${text} =    Open Browser     text is returned
    Should Be Equal    ${text}    text is returned

Oerwriting ElementFinder
    [Tags]    2
    ${element} =    Get WebElement    //div
    Should Be Equal    ${element}    Dummy find

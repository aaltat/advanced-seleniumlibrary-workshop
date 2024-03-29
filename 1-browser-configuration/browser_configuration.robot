*** Setting ***
Library           SeleniumLibrary
Suite Teardown    Close All Browsers

*** Test Case ***
Desired Capabilities As string
    [Tags]    1    grid
    Open Browser    https://robotframework.org/    Chrome
    ...    desired_capabilities=browserName:chrome,platform:WINDOWS

Desired Capabilities As Dictionary
    [Tags]    2
    ${desired_capabilities} =    Create Dictionary
    ...    browserName    chrome
    ...    platform       WINDOWS
    Open Browser    https://robotframework.org/    chrome
    ...    desired_capabilities=${desired_capabilities}

Browser Specific Selenium Options Attribute
    [Tags]    3    grid
    Open Browser    https://robotframework.org/    Chrome
    ...    options=headless=True
    Capture Page Screenshot

Browser Specific Selenium Options Method
    [Tags]    3
    Open Browser   https://robotframework.org/    Chrome
    ...    options=add_experimental_option("mobileEmulation", {'deviceName': 'Galaxy S5'});add_argument("--incognito")
    Capture Page Screenshot

Open Only One Browser
    [Tags]    5
    Open Browser    https://robotframework.org/    Chrome    alias=only_one
    Open Browser    https://github.com/robotframework/SeleniumLibrary    Chrome    alias=only_one
    ${locations} =    Get Locations    ALL
    Log    ${locations}

Create WebDriver With Headless
    [Tags]    6
    ${options}=	Evaluate	selenium.webdriver.ChromeOptions()	modules=selenium, selenium.webdriver
    ${options.add_argument}=	Set Variable	headless=True
    Create Webdriver	Chrome	options=${options}

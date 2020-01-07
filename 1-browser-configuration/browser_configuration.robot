*** Setting ***
Library           SeleniumLibrary
Suite Teardown    Close All Browsers

*** Test Case ***
Desired Capabilities As string
    [Tags]    1
    Open Browser    https://robocon.io/    Chrome    desired_capabilities=browserName:chrome,version:79,platform:Linux

Desired Capabilities As Dictionary
    [Tags]    2
    ${desired_capabilities} =    Create Dictionary
    ...    browserName    chrome
    ...    version        79
    ...    platform       Linux
    Open Browser    https://robocon.io/    Chrome    desired_capabilities=${desired_capabilities}

Browser Specific Selenium Options Attribute
    [Tags]    3
    Open Browser    https://robocon.io/    Chrome    options=headless=True
    Capture Page Screenshot

Browser Specific Selenium Options Method
    [Tags]    3
    Open Browser   https://robocon.io/    Chrome    options=add_experimental_option("mobileEmulation", {'deviceName': 'Galaxy S5'});add_argument("--incognito")
    Capture Page Screenshot

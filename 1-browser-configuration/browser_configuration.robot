*** Setting ***
Library           SeleniumLibrary
Suite Teardown    Close All Browsers

*** Variables ***
${REMOTE_URL}      ${False}

*** Test Case ***
Desired Capabilities As string
    [Tags]    1    grid
    Open Browser    https://robocon.io/    Chrome
    ...    desired_capabilities=browserName:chrome,platform:Linux
    ...    remote_url=${REMOTE_URL}

Desired Capabilities As Dictionary
    [Tags]    2
    ${desired_capabilities} =    Create Dictionary
    ...    browserName    chrome
    ...    platform       Linux
    Open Browser    https://robocon.io/    Chrome
    ...    desired_capabilities=${desired_capabilities}
    ...    remote_url=${REMOTE_URL}

Browser Specific Selenium Options Attribute
    [Tags]    3    grid
    Open Browser    https://robocon.io/    Chrome
    ...    options=headless=True
    ...    remote_url=${REMOTE_URL}
    Capture Page Screenshot

Browser Specific Selenium Options Method
    [Tags]    3
    Open Browser   https://robocon.io/    Chrome
    ...    options=add_experimental_option("mobileEmulation", {'deviceName': 'Galaxy S5'});add_argument("--incognito")
    ...    remote_url=${REMOTE_URL}
    Capture Page Screenshot

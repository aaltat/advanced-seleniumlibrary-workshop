*** Setting ***
Library           SeleniumLibrary
Library           DebugLibrary
Suite Teardown    Close All Browsers

*** Test Case ***
Browser Driver Logs To File
    [Tags]    2
    Open Browser   https://robocon.io/    Chrome    service_log_path=${OUTPUT_DIR}/chrome_driver.log
    Debug
    Wait Until Page Contains Element    //not_here
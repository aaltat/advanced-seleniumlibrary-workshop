*** Setting ***
Library           SeleniumLibrary
Suite Teardown    Close All Browsers

*** Test Case ***
Browser Driver Logs To File
    [Tags]    1
    Open Browser   https://robocon.io/    Chrome    service_log_path=${OUTPUT_DIR}/chrome_driver.log
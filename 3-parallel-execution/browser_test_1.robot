*** Setting ***
Library           SeleniumLibrary
Suite Setup       Open Browser    https://robotframework.org/    Chrome    remote_url=${REMOTE_URL}
Suite Teardown    Close All Browsers

*** Variables ***
${REMOTE_URL}    ${None}


*** Test Case ***
Browser Test 1-1
    [Tags]    1-1
    Page Should Contain Element    xpath://div

Browser Test 1-2
    [Tags]    1-2
    Capture Page Screenshot

Browser Test 1-3
    [Tags]    1-3
    ${url} =    Get Location
    Should Not Be Empty    ${url}

Browser test 1-4
    [Tags]    1-4
    Page Should Contain     RoboCon

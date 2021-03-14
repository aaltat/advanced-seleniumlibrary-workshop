*** Setting ***
Library           SeleniumLibrary
Suite Setup       Open Browser    https://robotframework.org/    Chrome    remote_url=${REMOTE_URL}
Suite Teardown    Close All Browsers

*** Variables ***
${REMOTE_URL}    ${None}


*** Test Case ***
Browser Test 2-1
    [Tags]    2-1
    Page Should Contain Element    xpath://div

Browser Test 2-2
    [Tags]    2-2
    Capture Page Screenshot

Browser Test 2-3
    [Tags]    2-3
    ${url} =    Get Location
    Should Not Be Empty    ${url}

Browser test 2-4
    [Tags]    2-4
    Page Should Contain     RoboCon

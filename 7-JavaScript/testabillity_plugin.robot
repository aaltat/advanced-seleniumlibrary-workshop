*** Setting ***
Library           SeleniumLibrary    plugins=SeleniumTestability;True;30 Seconds;True
Suite Teardown    Close All Browsers

*** Test Case ***
Testability Plugin
    [Tags]    1
    Open Browser    http://127.0.0.1:5000/welcome.html    Chrome
    Go To    http://127.0.0.1:5000/async.html
    Log To Console    Click id=animate-button
    Click Element    id=animate-button
    Log To Console    Click id=animateBox
    Click Element    id=animateBox
    Log To Console    *** DONE ***


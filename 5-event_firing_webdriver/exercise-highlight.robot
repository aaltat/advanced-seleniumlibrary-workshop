*** Settings ***
Library           SeleniumLibrary    # ???
Suite Teardown    Close All Browsers

*** Variables ***
${URL}        https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
${BROWSER}    Chrome

*** Test Cases ***
Highlight Clicking On Documentation Links
    Open Browser    ${URL}    ${BROWSER}
    Click Link  \#Add%20Location%20Strategy
    Click Link  \#Add%20Cookie

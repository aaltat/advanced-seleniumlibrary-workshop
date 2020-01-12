*** Settings ***
Library     pageobject.PageObject
Test Setup        Go To   Login
Suite Teardown    Close

*** Test Cases ***
Empty Passowrd
    Login    passowrd=${EMPTY}
    Location Should Be    Error
    Title Should Be Correct

Valid Login
    Login
    Location Should Be    Welcome
    Title Should Be Correct

Empty UserName
    Login    username=${EMPTY}
    Location Should Be    Error
    Title Should Be Correct

Invalid Username And Password
    Login    invalid    whatever
    Location Should Be    Error
    Title Should Be Correct

Empty Username And Password
    Login    ${EMPTY}    ${EMPTY}
    Location Should Be    Error
    Title Should Be Correct

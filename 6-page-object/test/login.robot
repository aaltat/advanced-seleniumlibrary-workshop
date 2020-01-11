*** Settings ***
Library     pageobject.PageObject
Test Setup        Go To   Login
Suite Teardown    Close

*** Test Cases ***
Valid Login
    Login

Empty Passowrd
    Login    passowrd=${EMPTY}       error=True

Empty UserName
    Login    username=${EMPTY}       error=True

Invalid Username And Password
    Login    invalid    whatever     error=True

Invalid Username
    Login    invalid                 error=True

Invalid Password
    Login    passowrd=invalid        error=True
Empty Username And Password
    Login    ${EMPTY}    ${EMPTY}    error=True

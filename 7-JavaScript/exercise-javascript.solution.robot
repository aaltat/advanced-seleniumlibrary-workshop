*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Using Javascript To Hide Floating Menu
    Open Browser    http://the-internet.herokuapp.com/floating_menu    Chrome
    Click Link      \#home
    Execute Javascript  document.getElementById("menu").style.display = 'none'
    Log To Console   Hide Menu
    Run Keyword And Expect Error  *  Click Link      \#home
    Execute Javascript  document.getElementById("menu").style.display = ''
    Log To Console  Revealed Menu
    Click Link      \#home
    
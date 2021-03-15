*** Setting ***
Library           DebugLibrary

*** Test Case ***
Walk Through The Debugger Commands
    [Tags]    3
    Debug
    Introduce The Debug Library
    Repeat After Me  RoboCon2021 is a Global Event
    The End Of The Test Case

*** Keywords ***
Introduce The Debug Library
    Log To Console  This is the debug library
    Log To Console  We can step through robot script
    Log  Or we can call keywords at the interactive prompt
    Hello World
    
Hello World
    Log To Console  Hello Nested World

Repeat After Me
    [Arguments]  ${echo}
    Log To Console  \nI say "${echo}"
    Log To Console  \n"${echo}" You reply

The End Of The Test Case
    Log To Console  \nThis is the end of the test case
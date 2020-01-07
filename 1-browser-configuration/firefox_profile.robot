*** Setting ***
Library           SeleniumLibrary
Variables         ff_profile_object.py
Suite Teardown    Close All Browsers

*** Test Case ***
FireFox Profile As Path
    [Tags]    10
    Open Browser    https://github.com/robotframework/SeleniumLibrary    Firefox    ff_profile_dir=/path/to/firefox/profile/dir

FireFox Profile As Object
    [Tags]    11
    Log Variables
    Open Browser    https://github.com/robotframework/SeleniumLibrary    Firefox    ff_profile_dir=${FF_PROFILE_AS_PYTHON_OBJECT}

FireFox Profile With Callin Method In Open Browser Keyword
    [Tags]    12
    ${methods_as_string} =    Catenate    SEPARATOR=;
    ...    set_preference("browser.download.folderList", 2)
    ...    set_preference("browser.download.manager.showWhenStarting", False)
    ...    set_preference("browser.download.dir", "${OUTPUT DIR}")
    ...    set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv,application/java-archive, application/x-msexcel,application/excel,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/x-excel,application/vnd.ms-excel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml,application/vnd.microsoft.portable-executable")
    Log    ${methods_as_string}
    Open Browser    https://github.com/robotframework/SeleniumLibrary    Firefox    ff_profile_dir=${methods_as_string}
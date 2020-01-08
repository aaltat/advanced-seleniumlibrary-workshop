*** Setting ***
Library           SeleniumLibrary
Variables         ff_profile_object.py
Suite Teardown    Close All Browsers

*** Variables ***
${REMOTE_URL}      ${False}

*** Test Case ***
FireFox Profile As Path
    [Tags]    10    grid
    Open Browser    https://github.com/robotframework/SeleniumLibrary    Firefox    ff_profile_dir=${FF_PROFILE_AS_DIR}
    ...    remote_url=${REMOTE_URL}

FireFox Profile As Object
    [Tags]    11
    Log Variables
    Open Browser    https://github.com/robotframework/SeleniumLibrary    Firefox    ff_profile_dir=${FF_PROFILE_AS_PYTHON_OBJECT}
    ...    remote_url=${REMOTE_URL}

FireFox Profile With Callin Method In Open Browser Keyword
    [Tags]    12
    ${methods_as_string} =    Catenate    SEPARATOR=;
    ...    set_preference("browser.download.folderList", 2)
    ...    set_preference("browser.download.manager.showWhenStarting", False)
    ...    set_preference("browser.download.dir", "${OUTPUT DIR}")
    ...    set_preference("browser.helperApps.neverAsk.saveToDisk", "image/png")
    Log    ${methods_as_string}
    Open Browser    https://github.com/robotframework/SeleniumLibrary    Firefox    ff_profile_dir=${methods_as_string}
    ...    remote_url=${REMOTE_URL}

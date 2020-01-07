from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver


def get_variables():
    ouptut = BuiltIn().get_variable_value('${OUTPUT DIR}')
    fp = webdriver.FirefoxProfile()
    fp.set_preference("browser.download.folderList", 2)
    fp.set_preference("browser.download.manager.showWhenStarting", False)
    fp.set_preference("browser.download.dir", ouptut)
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv,application/java-archive, application/x-msexcel,application/excel,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/x-excel,application/vnd.ms-excel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml,application/vnd.microsoft.portable-executable")
    return {'FF_PROFILE_AS_PYTHON_OBJECT': fp}

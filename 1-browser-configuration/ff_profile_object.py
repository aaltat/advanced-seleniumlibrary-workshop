from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver


def get_variables():
    ouptut = BuiltIn().get_variable_value('${OUTPUT DIR}')
    fp = webdriver.FirefoxProfile()
    fp.set_preference("browser.download.folderList", 2)
    fp.set_preference("browser.download.manager.showWhenStarting", False)
    fp.set_preference("browser.download.dir", ouptut)
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "image/png")
    fp.update_preferences()
    return {'FF_PROFILE_AS_PYTHON_OBJECT': fp, 'FF_PROFILE_AS_DIR': fp.path}

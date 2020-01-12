from pageobject.pageobject import CTX


class Error(CTX):

    def __init__(self):
        CTX.__init__(self)
        self.page_url = '%serror.html' % self.host

    def title_should_be_correct(self):
        title = self.driver.title
        assert title == 'Error Page'

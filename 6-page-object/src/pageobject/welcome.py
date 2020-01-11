from pageobject.pageobject import CTX


class Welcome(CTX):

    def __init__(self):
        CTX.__init__(self)
        self.page_url = '%swelcome.html' % self.host

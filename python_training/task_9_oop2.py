class Page:

    def __init__(self, url):
        self.url = url

    def get(self):
        print(self.url)


home = Page('www.134.ru')
home.get()

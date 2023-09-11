class ButtonTest:

    type: str = 'Кнопка'

    def __init__(self, text, link):
        self.text = text
        self.link = link

# создаем экземпляры класса


home = ButtonTest('Домой', '/home')
catalog_msk = ButtonTest('Каталог', '/msk/catalog')

# получаем доступ к атрибутам

print(home.text)
print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)

print('\n')

print(catalog_msk.text)
print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)
print(home.type)
print(catalog_msk.type)


class ButtonTwo:
    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)


# создаем экз. класса
home_two = ButtonTwo('Домой', '/home', 'button#home')
# вызываем метод
print(home_two.click())


class Input:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


search = Input('hgsfhtrsnjsrt', 'текст')

print(search.loc)


class Title:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


class Link:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


class Button:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


obj1 = Input('лок1', 'текст1')
obj2 = Button('лок2', 'текст2')
obj3 = Title('лок3', 'текст3')
obj4 = Link('лок4', 'текст4')

print(obj1.text + ' ' + obj1.loc + ' ' + obj2.text + ' ' + obj2.loc +
      ' ' + obj3.text + ' ' + obj3.loc + ' ' + obj4.text + ' ' + obj4.loc)


from python_training.task_9_checks import Checks


class Input(Checks):
    def __int__(self, loc):
        super().__init__(loc)

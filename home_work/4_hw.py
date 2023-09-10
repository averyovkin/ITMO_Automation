class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height


R1 = Rectangle(5, 10)
R2 = Rectangle(343, 44)
R3 = Rectangle(11111, 222222)

S1 = R1.width * R1.height
P1 = 2 * (R1.width + R1.height)
S2 = R2.width * R2.height
P2 = 2 * (R2.width + R2.height)
S3 = R3.width * R3.height
P3 = 2 * (R3.width + R3.height)

print(f'площади: ', S1, S2, S3)
print(f'периметры:',  P1, P2, P3)


class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(f'a + b = {self.a + self.b}')

    def multiplication(self):
        print(f'a * b = {self.a * self.b}')

    def division(self):
        print(f'a / b = {self.a / self.b}')

    def substraction(self):
        print(f'a - b = {self.a - self.b}')


X = Math(3, 4)
print('a = ', X.a, '    ', 'b = ', X.b)
X.addition()
X.division()
X.substraction()
X.multiplication()


class Button:

    def __init__(self, tip, text, loc=None):
        self.tip = tip
        self.text = text
        self.loc = loc

    def click(self):
        return "Клик по кнопке {}".format(self.text)


ob1 = Button('Кнопка', 'Text Box')
ob2 = Button('Кнопка', 'Check box')
ob3 = Button('Кнопка', 'Radio Button')
ob4 = Button('Кнопка', 'Web Tables')
ob5 = Button('Кнопка', 'Buttons')
ob6 = Button('Кнопка', 'Links')
ob7 = Button('Кнопка', 'Broken Links - Images')
ob8 = Button('Кнопка', 'Upload and Download')
ob9 = Button('Кнопка', 'Dynamic Properties')

print(ob1.text)
print(ob1.click())

print(ob2.text)
print(ob2.click())

print(ob3.text)
print(ob3.click())

print(ob4.text)
print(ob4.click())

print(ob5.text)
print(ob5.click())

print(ob6.text)
print(ob6.click())

print(ob7.text)
print(ob7.click())

print(ob8.text)
print(ob8.click())

print(ob9.text)
print(ob9.click())
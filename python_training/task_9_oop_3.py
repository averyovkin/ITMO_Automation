class Soda:

    def __init__(self, dop=None):
        self.dop = dop

    def show_my_drink(self):
        if self.dop:
            print('Газировка и {}'.format(self.dop))
            # либо так print(f'Газировка и {self.dop}')
        else:
            print('Обычная газирвока')


drink1 = Soda('кола')
drink2 = Soda()

drink1.show_my_drink()
drink2.show_my_drink()

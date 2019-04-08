
class Car:

    def __init__(self, make_in, model_in, cc_in):
        self.make = make_in
        self.model = model_in
        self.cc = cc_in

    def print(self):
        print('Make     ', self.make)
        print('model    ', self.model)
        print('CC       ', self.cc)


class RaceCar(Car):

    def __init__(self, make_in, model_in, cc_in, race_won_in):
        super().__init__(make_in, model_in, cc_in)
        self.race_won = race_won_in

    def print(self):
        super().print()
        print('Races Won', self.race_won)


car1 = Car('ford', 'fiesta', 1200)
car1.print()

car2 = RaceCar('Ford', 'Focus ST', 2400, 13)
car2.print()

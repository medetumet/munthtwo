class Hero:
    Head = 1
    ability = True

    def __init__(self, name, nickname, hp, damage):
        self.name = name
        self.nickname = nickname
        self.hp = hp
        self.damage = damage

    def heal(self):
        self.hp += 100

    def two_damage(self):
        self.damage *= 2

    def greetings(self):
        print(f'my name is {self.name}')

    def brand_phrase(self):
        print('good will win')


hero1 = Hero('Meepo', 'mepep', 450, 38)
hero2 = Hero('Invoker', 'inv4005', 360, 26)
hero3 = Hero('Zemelya', 'groom65', 600, 25)
hero4 = Hero('Pudje', 'pudj2005', 230, 60)

hero1.heal()
hero2.two_damage()
hero3.greetings()
hero4.brand_phrase()


class Airhero(Hero):
    fly = False

    def __init__(self, name, nickname, hp, damage, fly=False):
        super().__init__(name, nickname, hp, damage)
        self.fly = fly

    def brand_phrase(self):
        self.fly = True
        print(f'fly in the True_phrase')

    def __Gen_x(self):
        pass


Airhero1 = Airhero('Asyl', 'asyl312', 100, 15)
Airhero1.brand_phrase()


class Earthhero(Hero):
    fly = False

    def __init__(self, name, nickname, hp, damage, fly=False):
        super().__init__(name, nickname, hp, damage)
        self.fly = fly

    def brand_phrase(self):
        self.fly = True
        print(f'fly in the True_phrase')

    def __Gen_x(self):
        pass


Erthhero1 = Earthhero('Medet', 'medet888', 200, 37)
Erthhero1.brand_phrase()


class Cosmichero(Hero):
    fly = False

    def __init__(self, name, nickname, hp, damage, fly=False):
        super().__init__(name, nickname, hp, damage)
        self.fly = fly

    def brand_phrase(self):
        self.fly = True
        print(f'fly in the True_phrase')

    def __Gen_x(self):
        pass


Cosmichero1 = Cosmichero('Amir', 'amir777', 300, 12)
Cosmichero1.brand_phrase()

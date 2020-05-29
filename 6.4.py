class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехал'

    def stop(self):
        return f'{self.name} остановился'

    def turn(self,):
            return f'{self.name} повернул'

    #def turn(self, direction)
        #d = ['налево', 'направо']
        #direction = []
        #for i in d:
            #return f'{self.name} повернул {direction.remove(i)}'

    def show_speed(self):
        return f'Текущая скорость {self.name} = {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print (f'Текущая скорость {self.name} = {self.speed}')

        if self.speed > 60:
            return f'Превышение скорости для {self.name}'
        else:
            return f'Допустимый уровень скорости для {self.name}'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print (f'Текущая скорость {self.name} = {self.speed}')

        if self.speed > 40:
            return f'Превышение скорости для {self.name}'
        else:
            return f'Допустимый уровень скорости для {self.name}'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} машина полиции'
        else:
            return f' '

t = TownCar(80, 'серебряный', 'BMW', False)
s = SportCar(120, 'черный', 'Porshe', False)
w = WorkCar(35, 'белый', 'Kamaz', False)
p = PoliceCar(90, 'черный', 'Ford', True)
print(f'{t.speed}, {t.color}, {t.name}, {t.is_police}')
print(f'{p.speed}, {p.color}, {p.name}, {p.is_police}')
print(f'{w.go()}, {w.turn()}, {w.stop()}')
print(t.show_speed())
print(w.show_speed())
print(p.police())




class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print('go forward')

    def stop(self):
        print('car stopped')

    def turn(self, direction):
        print(f'turn {direction}')

    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'speed = {self.speed} OVER SPEED')
        else:
            print(f'speed = {self.speed}')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'speed = {self.speed} OVER SPEED')
        else:
            print(f'speed = {self.speed}')

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass


town_car = TownCar(150, 'red', 'kia', False)

town_car.turn('left')
town_car.show_speed()

work_car = WorkCar(30, 'green', 'KAMAZ', False)
work_car.show_speed()
print(work_car.name)

sport_car = SportCar(250, 'red', 'Ferrari', False)
sport_car.show_speed()

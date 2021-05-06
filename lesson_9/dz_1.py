import time


class TrafficLight:
    __color = 'red'
    def running(self):
        print(TrafficLight.__color)
        time.sleep(7)
        TrafficLight.__color = 'yellow'
        print(TrafficLight.__color)
        time.sleep(2)
        TrafficLight.__color = 'green'
        print(TrafficLight.__color)
        time.sleep(5)
        TrafficLight.__color = 'red'


traffic_light = TrafficLight()

traffic_light.running()
traffic_light.running()
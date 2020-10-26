import time

class TrafficLight:
    __color = ''

    def running():
        while True:
            TrafficLight.color = 'RED'
            print(TrafficLight.color)
            time.sleep(7)
            TrafficLight.color = 'YELLOW'
            print(TrafficLight.color)
            time.sleep(2)
            TrafficLight.color = 'GREEN'
            print(TrafficLight.color)
            time.sleep(5)


TrafficLight.running()

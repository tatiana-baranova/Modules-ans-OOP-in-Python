class Transport:
    def __init__(self, speed, weight, isWorking):
        self.speed = speed
        self.weight = weight
        self.isWorking = isWorking
        # self.get_info()

    def get_info(self):
        work = "Working" if self.isWorking else "Not Working"
        print(f"Speed: {self.speed}, weight: {self.weight}. Is Working: {work}")

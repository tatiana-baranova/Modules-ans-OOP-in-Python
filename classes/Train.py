from classes.Transport import Transport as Tr
class Train(Tr):
    def __init__(self, speed:int, weight:int, isWorking:bool, wagon_count:int):
        super(Train, self).__init__(speed, weight, isWorking)
        self.wagon_count = wagon_count
    def get_info(self):
        super().get_info()
        print(f"Wagon count: {self.wagon_count}")
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from classes.Car import Car
from classes.Train import Train
from classes.Ship import Ship


bmw = Car(200, 2000, True)
train = Train(140, 20000, False, 5)
ship = Ship(50, 5000, True)
train.get_info()
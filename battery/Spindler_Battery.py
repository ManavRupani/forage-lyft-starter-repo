from abc import ABC

from car import Car


class SpinderBattery(Car, ABC):
    def __init__(self, last_service_date, currrent_date):
        super().__init__(last_service_date)
        self.current_date= current_date
        self.last_service_mileage = last_service_mileage

    def battery_should_be_serviced(self):
        return self.c

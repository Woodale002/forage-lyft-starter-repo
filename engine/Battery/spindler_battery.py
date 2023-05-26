from abc import ABC

from car import Car


class Spindler_Battery(Car, ABC):
    def __init__(self, last_service_date, current_year, last_service_yaer:
        super().__init__(last_service_date)
        self.current_data= current_date
        self.last_service_mileage = last_service_mileage

    def battery_should_be_serviced(self):
        return self.current_day - self.last_service_day > 4

"""Car Factory"""
from datetime import datetime  # noqa

from battery import NubbinBattery, SpindlerBattery
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from car import Car


class CarFactory:
    """An abstract CarFactory class."""
    @staticmethod
    def _create_calliope(current_date, last_service_date,
                         current_mileage, last_service_mileage) -> Car:
        """Create a Calliope model."""
        battery = SpindlerBattery(last_service_date,
                                  current_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        return Car(battery, engine)

    @staticmethod
    def _create_glissade(current_date, last_service_date, current_mileage,
                         last_service_mileage) -> Car:
        """Create a Glissade model."""
        battery = SpindlerBattery(last_service_date,
                                  current_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return Car(battery, engine)

    @staticmethod
    def _create_palindrome(current_date, last_service_date,
                           warning_light_on) -> Car:
        battery = SpindlerBattery(last_service_date,
                                  current_date)
        engine = SternmanEngine(warning_light_on)
        return Car(battery, engine)

    @staticmethod
    def _create_rorschach(current_date, last_service_date, current_mileage,
                          last_service_mileage) -> Car:
        battery = NubbinBattery(last_service_date, current_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return Car(battery, engine)

    @staticmethod
    def _create_thovex(current_date, last_service_date, current_mileage,
                       last_service_mileage) -> Car:
        battery = NubbinBattery(last_service_date, current_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        return Car(battery, engine)

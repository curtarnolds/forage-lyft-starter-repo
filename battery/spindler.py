"""A nubbin module for SpindlerBattery class."""
from datetime import datetime

from battery_abc import Battery


class SpindlerBattery(Battery):
    """A SpindlerBattery class."""

    def __init__(self, last_service_date=datetime.today().date(),
                 current_date=datetime.today().date()):
        """Initialize a SpindlerBattery instance.

        Args:
            last_service_date (datetime): The date the battery was last
            serviced. Defalts to current date.

            current_date (datetime): The current date.
        """
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        """Check if battery needs to be serviced."""
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + 2)
        return (service_threshold_date < self.current_date)

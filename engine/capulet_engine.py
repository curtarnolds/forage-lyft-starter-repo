from engine_abc import Engine


class CapuletEngine(Engine):
    def __init__(self, current_mileage=0,
                 last_service_mileage=0):
        """Initialize a CapuletEngine.

        Args:
        current_mileage (int): The current mileage of the engine
        last_service_mileage (int): The mileage as at the last servicing
        """
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        mileage_since_last_service = self.current_mileage\
            - self.last_service_mileage
        return mileage_since_last_service > 30000
